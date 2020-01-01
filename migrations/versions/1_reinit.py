"""reinit

Revision ID: 1
Revises: 
Create Date: 2020-01-01 22:59:10.872705

"""
from alembic import op
import sqlalchemy as sa
import lazyblacksmith

# revision identifiers, used by Alembic.
revision = '1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('item',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('max_production_limit', sa.Integer(), nullable=True),
    sa.Column('market_group_id', sa.Integer(), nullable=True),
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('volume', sa.Numeric(precision=16, scale=4, decimal_return_scale=4, asdecimal=False), nullable=True),
    sa.Column('is_from_manufacturing', sa.Boolean(), nullable=True),
    sa.Column('is_from_reaction', sa.Boolean(), nullable=True),
    sa.Column('base_cost', sa.Numeric(precision=17, scale=2, decimal_return_scale=2, asdecimal=False), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('item_adjusted_price',
    sa.Column('item_id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('price', sa.Numeric(precision=17, scale=2, decimal_return_scale=2, asdecimal=False), nullable=True),
    sa.PrimaryKeyConstraint('item_id')
    )
    op.create_table('item_price',
    sa.Column('item_id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('region_id', sa.Integer(), nullable=False),
    sa.Column('sell_price', sa.Numeric(precision=17, scale=2, decimal_return_scale=2, asdecimal=False), nullable=True),
    sa.Column('buy_price', sa.Numeric(precision=17, scale=2, decimal_return_scale=2, asdecimal=False), nullable=True),
    sa.Column('updated_at', lazyblacksmith.models.utcdatetime.UTCDateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('item_id', 'region_id')
    )
    op.create_table('region',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('wh', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('task_state',
    sa.Column('task_id', sa.String(length=250), nullable=False),
    sa.Column('id', sa.BigInteger(), nullable=True),
    sa.Column('scope', sa.String(length=100), nullable=True),
    sa.Column('state', sa.String(length=20), nullable=True),
    sa.Column('start_date', lazyblacksmith.models.utcdatetime.UTCDateTime(timezone=True), nullable=True),
    sa.Column('end_date', lazyblacksmith.models.utcdatetime.UTCDateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('task_id')
    )
    op.create_table('user',
    sa.Column('character_id', sa.BigInteger(), autoincrement=False, nullable=False),
    sa.Column('character_owner_hash', sa.String(length=255), nullable=True),
    sa.Column('character_name', sa.String(length=200), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.Column('is_corp_director', sa.Boolean(), nullable=True),
    sa.Column('corporation_id', sa.BigInteger(), nullable=True),
    sa.Column('current_login_at', lazyblacksmith.models.utcdatetime.UTCDateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('created_at', lazyblacksmith.models.utcdatetime.UTCDateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', lazyblacksmith.models.utcdatetime.UTCDateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('main_character_id', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['main_character_id'], ['user.character_id'], ),
    sa.PrimaryKeyConstraint('character_id')
    )
    op.create_table('activity',
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('time', sa.Integer(), nullable=True),
    sa.Column('activity', sa.Integer(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['item_id'], ['item.id'], ),
    sa.PrimaryKeyConstraint('item_id', 'activity')
    )
    op.create_table('activity_material',
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('activity', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('material_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['item_id'], ['item.id'], ),
    sa.ForeignKeyConstraint(['material_id'], ['item.id'], ),
    sa.PrimaryKeyConstraint('item_id', 'activity', 'material_id')
    )
    op.create_table('activity_product',
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('activity', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('probability', sa.Numeric(precision=3, scale=2, decimal_return_scale=2, asdecimal=False), nullable=True),
    sa.ForeignKeyConstraint(['item_id'], ['item.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['item.id'], ),
    sa.PrimaryKeyConstraint('item_id', 'activity', 'product_id')
    )
    op.create_table('activity_skill',
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('activity', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('skill_id', sa.Integer(), nullable=False),
    sa.Column('level', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['item_id'], ['item.id'], ),
    sa.ForeignKeyConstraint(['skill_id'], ['item.id'], ),
    sa.PrimaryKeyConstraint('item_id', 'activity', 'skill_id')
    )
    op.create_table('blueprint',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item_id', sa.Integer(), nullable=True),
    sa.Column('character_id', sa.BigInteger(), nullable=True),
    sa.Column('original', sa.Boolean(), nullable=False),
    sa.Column('total_runs', sa.Integer(), nullable=False),
    sa.Column('material_efficiency', sa.Integer(), nullable=False),
    sa.Column('time_efficiency', sa.Integer(), nullable=False),
    sa.Column('corporation', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['character_id'], ['user.character_id'], ),
    sa.ForeignKeyConstraint(['item_id'], ['item.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('constellation',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('region_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['region_id'], ['region.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('decryptor',
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('probability_multiplier', sa.Numeric(precision=4, scale=2, decimal_return_scale=2, asdecimal=False), nullable=True),
    sa.Column('material_modifier', sa.Integer(), nullable=True),
    sa.Column('time_modifier', sa.Integer(), nullable=True),
    sa.Column('run_modifier', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['item_id'], ['item.id'], ),
    sa.PrimaryKeyConstraint('item_id')
    )
    op.create_table('ore_refining',
    sa.Column('ore_id', sa.Integer(), nullable=False),
    sa.Column('material_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('batch', sa.Integer(), nullable=True),
    sa.Column('is_compressed', sa.Boolean(), nullable=True),
    sa.Column('is_ice', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['material_id'], ['item.id'], ),
    sa.ForeignKeyConstraint(['ore_id'], ['item.id'], ),
    sa.PrimaryKeyConstraint('ore_id', 'material_id')
    )
    op.create_table('skill',
    sa.Column('skill_id', sa.Integer(), nullable=False),
    sa.Column('character_id', sa.BigInteger(), nullable=False),
    sa.Column('level', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['character_id'], ['user.character_id'], ),
    sa.ForeignKeyConstraint(['skill_id'], ['item.id'], ),
    sa.PrimaryKeyConstraint('skill_id', 'character_id')
    )
    op.create_table('token_scope',
    sa.Column('user_id', sa.BigInteger(), nullable=False),
    sa.Column('scope', sa.String(length=250), nullable=False),
    sa.Column('access_token', sa.String(length=4096), nullable=True),
    sa.Column('access_token_expires', lazyblacksmith.models.utcdatetime.UTCDateTime(timezone=True), nullable=True),
    sa.Column('refresh_token', sa.String(length=100), nullable=True),
    sa.Column('last_update', lazyblacksmith.models.utcdatetime.UTCDateTime(timezone=True), nullable=True),
    sa.Column('cached_until', lazyblacksmith.models.utcdatetime.UTCDateTime(timezone=True), nullable=True),
    sa.Column('valid', sa.Boolean(), nullable=True),
    sa.Column('request_try', sa.Integer(), nullable=True),
    sa.Column('created_at', lazyblacksmith.models.utcdatetime.UTCDateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', lazyblacksmith.models.utcdatetime.UTCDateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.character_id'], ),
    sa.PrimaryKeyConstraint('user_id', 'scope')
    )
    op.create_table('user_preference',
    sa.Column('user_id', sa.BigInteger(), nullable=False),
    sa.Column('invention_facility', sa.Integer(), server_default='0', nullable=False),
    sa.Column('invention_invention_rig', sa.Integer(), server_default='0', nullable=False),
    sa.Column('invention_copy_rig', sa.Integer(), server_default='0', nullable=False),
    sa.Column('invention_security', sa.String(length=1), server_default='h', nullable=False),
    sa.Column('invention_system', sa.String(length=100), server_default='Jita', nullable=False),
    sa.Column('invention_price_region', sa.Integer(), server_default='10000002', nullable=False),
    sa.Column('invention_price_type', sa.String(length=4), server_default='buy', nullable=False),
    sa.Column('invention_character_id', sa.BigInteger(), nullable=True),
    sa.Column('invention_copy_implant', sa.Numeric(precision=3, scale=2, decimal_return_scale=2, asdecimal=False), server_default='1.00', nullable=False),
    sa.Column('research_facility', sa.Integer(), server_default='0', nullable=False),
    sa.Column('research_me_rig', sa.Integer(), server_default='0', nullable=False),
    sa.Column('research_te_rig', sa.Integer(), server_default='0', nullable=False),
    sa.Column('research_copy_rig', sa.Integer(), server_default='0', nullable=False),
    sa.Column('research_security', sa.String(length=1), server_default='h', nullable=False),
    sa.Column('research_system', sa.String(length=100), server_default='Jita', nullable=False),
    sa.Column('research_character_id', sa.BigInteger(), nullable=True),
    sa.Column('research_me_implant', sa.Numeric(precision=3, scale=2, decimal_return_scale=2, asdecimal=False), server_default='1.00', nullable=False),
    sa.Column('research_te_implant', sa.Numeric(precision=3, scale=2, decimal_return_scale=2, asdecimal=False), server_default='1.00', nullable=False),
    sa.Column('research_copy_implant', sa.Numeric(precision=3, scale=2, decimal_return_scale=2, asdecimal=False), server_default='1.00', nullable=False),
    sa.Column('prod_facility', sa.Integer(), server_default='0', nullable=False),
    sa.Column('prod_me_rig', sa.Integer(), server_default='0', nullable=False),
    sa.Column('prod_te_rig', sa.Integer(), server_default='0', nullable=False),
    sa.Column('prod_security', sa.String(length=1), server_default='h', nullable=False),
    sa.Column('prod_system', sa.String(length=100), server_default='Jita', nullable=False),
    sa.Column('prod_sub_facility', sa.Integer(), server_default='0', nullable=False),
    sa.Column('prod_sub_me_rig', sa.Integer(), server_default='0', nullable=False),
    sa.Column('prod_sub_te_rig', sa.Integer(), server_default='0', nullable=False),
    sa.Column('prod_sub_security', sa.String(length=1), server_default='h', nullable=False),
    sa.Column('prod_sub_system', sa.String(length=100), server_default='Jita', nullable=False),
    sa.Column('prod_price_region_minerals', sa.Integer(), server_default='10000002', nullable=False),
    sa.Column('prod_price_region_pi', sa.Integer(), server_default='10000002', nullable=False),
    sa.Column('prod_price_region_moongoo', sa.Integer(), server_default='10000002', nullable=False),
    sa.Column('prod_price_region_others', sa.Integer(), server_default='10000002', nullable=False),
    sa.Column('prod_price_type_minerals', sa.String(length=4), server_default='buy', nullable=False),
    sa.Column('prod_price_type_pi', sa.String(length=4), server_default='buy', nullable=False),
    sa.Column('prod_price_type_moongoo', sa.String(length=4), server_default='buy', nullable=False),
    sa.Column('prod_price_type_others', sa.String(length=4), server_default='buy', nullable=False),
    sa.Column('prod_character_id', sa.BigInteger(), nullable=True),
    sa.Column('prod_te_implant', sa.Numeric(precision=3, scale=2, decimal_return_scale=2, asdecimal=False), server_default='1.00', nullable=False),
    sa.Column('reaction_facility', sa.Integer(), server_default='5', nullable=False),
    sa.Column('reaction_me_rig', sa.Integer(), server_default='0', nullable=False),
    sa.Column('reaction_te_rig', sa.Integer(), server_default='0', nullable=False),
    sa.Column('reaction_security', sa.String(length=1), server_default='l', nullable=False),
    sa.Column('reaction_system', sa.String(length=100), server_default='Rakapas', nullable=False),
    sa.Column('reaction_manuf_facility', sa.Integer(), server_default='0', nullable=False),
    sa.Column('reaction_manuf_me_rig', sa.Integer(), server_default='0', nullable=False),
    sa.Column('reaction_manuf_te_rig', sa.Integer(), server_default='0', nullable=False),
    sa.Column('reaction_manuf_security', sa.String(length=1), server_default='h', nullable=False),
    sa.Column('reaction_manuf_system', sa.String(length=100), server_default='Jita', nullable=False),
    sa.Column('reaction_manuf_te_implant', sa.Numeric(precision=3, scale=2, decimal_return_scale=2, asdecimal=False), server_default='1.00', nullable=False),
    sa.Column('reaction_price_regions', sa.Integer(), server_default='10000002', nullable=False),
    sa.Column('reaction_price_type', sa.String(length=4), server_default='buy', nullable=False),
    sa.Column('reaction_character_id', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['invention_character_id'], ['user.character_id'], ),
    sa.ForeignKeyConstraint(['prod_character_id'], ['user.character_id'], ),
    sa.ForeignKeyConstraint(['reaction_character_id'], ['user.character_id'], ),
    sa.ForeignKeyConstraint(['research_character_id'], ['user.character_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.character_id'], ),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('solar_system',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('region_id', sa.Integer(), nullable=True),
    sa.Column('constellation_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['constellation_id'], ['constellation.id'], ),
    sa.ForeignKeyConstraint(['region_id'], ['region.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('industry_index',
    sa.Column('solarsystem_id', sa.Integer(), nullable=False),
    sa.Column('activity', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('cost_index', sa.Numeric(precision=20, scale=19, decimal_return_scale=19, asdecimal=False), nullable=True),
    sa.ForeignKeyConstraint(['solarsystem_id'], ['solar_system.id'], ),
    sa.PrimaryKeyConstraint('solarsystem_id', 'activity')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('industry_index')
    op.drop_table('solar_system')
    op.drop_table('user_preference')
    op.drop_table('token_scope')
    op.drop_table('skill')
    op.drop_table('ore_refining')
    op.drop_table('decryptor')
    op.drop_table('constellation')
    op.drop_table('blueprint')
    op.drop_table('activity_skill')
    op.drop_table('activity_product')
    op.drop_table('activity_material')
    op.drop_table('activity')
    op.drop_table('user')
    op.drop_table('task_state')
    op.drop_table('region')
    op.drop_table('item_price')
    op.drop_table('item_adjusted_price')
    op.drop_table('item')
    # ### end Alembic commands ###
