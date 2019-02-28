from indy_common.authorize.auth_actions import ADD_PREFIX
from indy_common.constants import AUTH_RULE, CONSTRAINT, AUTH_ACTION, AUTH_TYPE, FIELD, NEW_VALUE, OLD_VALUE, NYM, \
    TRUST_ANCHOR
from plenum.common.constants import TRUSTEE, TXN_TYPE

from indy_common.authorize.auth_constraints import CONSTRAINT_ID, ROLE, SIG_COUNT, NEED_TO_BE_OWNER, METADATA, \
    ConstraintsEnum, AUTH_CONSTRAINTS


def generate_constraint_entity(constraint_id=ConstraintsEnum.ROLE_CONSTRAINT_ID,
                               role=TRUSTEE,
                               sig_count=1,
                               need_to_be_owner=False,
                               metadata={}):
    return {CONSTRAINT_ID: constraint_id,
            ROLE: role,
            SIG_COUNT: sig_count,
            NEED_TO_BE_OWNER: need_to_be_owner,
            METADATA: metadata}


def generate_constraint_list(constraint_id=ConstraintsEnum.AND_CONSTRAINT_ID,
                             auth_constraints=None):
    auth_constraints = generate_constraint_entity() \
        if auth_constraints is None \
        else auth_constraints
    return {CONSTRAINT_ID: constraint_id,
            AUTH_CONSTRAINTS: auth_constraints}


def generate_auth_rule_operation(auth_action=ADD_PREFIX, auth_type=NYM,
                                 field=ROLE, new_value=TRUST_ANCHOR,
                                 old_value=None, constraint=None):
    constraint = generate_constraint_entity() \
        if constraint is None \
        else constraint
    op = {TXN_TYPE: AUTH_RULE,
          CONSTRAINT: constraint,
          AUTH_ACTION: auth_action,
          AUTH_TYPE: auth_type,
          FIELD: field,
          NEW_VALUE: new_value
          }
    if old_value:
        op[OLD_VALUE] = old_value
    return op
