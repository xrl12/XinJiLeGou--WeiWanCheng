"""addShop

Revision ID: ef04a4615417
Revises: 
Create Date: 2020-06-10 15:21:44.217666

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef04a4615417'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('AdminUser',
    sa.Column('create_time', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.Column('update_time', sa.DateTime(), nullable=True, comment='跟新时间'),
    sa.Column('status', sa.Boolean(), nullable=True, comment='是否被冻结'),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=32), nullable=True, comment='员工名字'),
    sa.Column('group', sa.String(length=32), nullable=True, comment='员工是那个部门的'),
    sa.Column('password', sa.String(length=100), nullable=True, comment='登录密码'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('area',
    sa.Column('create_time', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.Column('update_time', sa.DateTime(), nullable=True, comment='跟新时间'),
    sa.Column('status', sa.Boolean(), nullable=True, comment='是否被冻结'),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False, comment='区域：比如，发现好物'),
    sa.Column('position', sa.Integer(), nullable=False, comment='所在在位置是否考前'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('brank',
    sa.Column('create_time', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.Column('update_time', sa.DateTime(), nullable=True, comment='跟新时间'),
    sa.Column('status', sa.Boolean(), nullable=True, comment='是否被冻结'),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False, comment='品牌'),
    sa.Column('first_letter', sa.String(length=32), nullable=False, comment='品牌的首字母'),
    sa.Column('logo', sa.String(length=200), nullable=False, comment='logo图片链接'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('category',
    sa.Column('create_time', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.Column('update_time', sa.DateTime(), nullable=True, comment='跟新时间'),
    sa.Column('status', sa.Boolean(), nullable=True, comment='是否被冻结'),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('position', sa.Integer(), nullable=False),
    sa.Column('show_page', sa.Integer(), nullable=False),
    sa.Column('area_id', sa.Integer(), nullable=False, comment='属于那个区域的'),
    sa.Column('own', sa.Integer(), nullable=False, comment='二级分类进关联一级分类'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('member',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nickname', sa.String(length=100), nullable=False, comment='昵称'),
    sa.Column('mobile', sa.String(length=11), nullable=False, comment='手机号'),
    sa.Column('gender', sa.Integer(), nullable=False, comment='性别'),
    sa.Column('avatar', sa.String(length=200), nullable=False, comment='头像url'),
    sa.Column('salt', sa.String(length=32), nullable=False),
    sa.Column('reg_ip', sa.String(length=100), nullable=False, comment='注册ip'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('shopdetailimage',
    sa.Column('create_time', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.Column('update_time', sa.DateTime(), nullable=True, comment='跟新时间'),
    sa.Column('status', sa.Boolean(), nullable=True, comment='是否被冻结'),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='唯一标示'),
    sa.Column('img', sa.String(length=100), nullable=False, comment='详情图的url地址'),
    sa.Column('shop_sku_id', sa.Integer(), nullable=False, comment='所关联的商品'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('shopguigeinfo',
    sa.Column('create_time', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.Column('update_time', sa.DateTime(), nullable=True, comment='跟新时间'),
    sa.Column('status', sa.Boolean(), nullable=True, comment='是否被冻结'),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='主键，唯一标识'),
    sa.Column('sku_id', sa.Integer(), nullable=False, comment='商品sku的id'),
    sa.Column('guigekey', sa.Integer(), nullable=False, comment='商品规格的键的ID'),
    sa.Column('guigevlaue', sa.Integer(), nullable=False, comment='商品规格值的ID'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('shopguigekey',
    sa.Column('create_time', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.Column('update_time', sa.DateTime(), nullable=True, comment='跟新时间'),
    sa.Column('status', sa.Boolean(), nullable=True, comment='是否被冻结'),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='主键，唯一标识'),
    sa.Column('shop_id', sa.Integer(), nullable=False, comment='商品的主键,'),
    sa.Column('name', sa.String(length=32), nullable=False, comment='商品属性的名字'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('shopguigevalue',
    sa.Column('create_time', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.Column('update_time', sa.DateTime(), nullable=True, comment='跟新时间'),
    sa.Column('status', sa.Boolean(), nullable=True, comment='是否被冻结'),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='主键，唯一标识'),
    sa.Column('value', sa.String(length=32), nullable=False, comment='属性值'),
    sa.Column('key_id', sa.Integer(), nullable=False, comment='商品规格的键进行关联'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('shopsku',
    sa.Column('create_time', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.Column('update_time', sa.DateTime(), nullable=True, comment='跟新时间'),
    sa.Column('status', sa.Boolean(), nullable=True, comment='是否被冻结'),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='主键，唯一标识'),
    sa.Column('name', sa.String(length=32), nullable=False, comment='sku的名字'),
    sa.Column('price', sa.DECIMAL(precision=8, scale=2), nullable=False, comment='商品的售价'),
    sa.Column('cost_price', sa.DECIMAL(precision=8, scale=2), nullable=False, comment='商品的进价'),
    sa.Column('market_price', sa.DECIMAL(precision=8, scale=2), nullable=False, comment='商品的市场价'),
    sa.Column('stock', sa.Integer(), nullable=False, comment='库存'),
    sa.Column('salas', sa.Integer(), nullable=False, comment='销量'),
    sa.Column('comments', sa.Integer(), nullable=False, comment='评论量'),
    sa.Column('is_launched', sa.Boolean(), nullable=False, comment='是否上架'),
    sa.Column('default_img_url', sa.String(length=100), nullable=False, comment='主页图片的路由'),
    sa.Column('shop_id', sa.Integer(), nullable=False, comment='进行关联的商品的id'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('shopspu',
    sa.Column('create_time', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.Column('update_time', sa.DateTime(), nullable=True, comment='跟新时间'),
    sa.Column('status', sa.Boolean(), nullable=True, comment='是否被冻结'),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False, comment='商品名字'),
    sa.Column('sales', sa.Integer(), nullable=False, comment='销量'),
    sa.Column('comments', sa.Integer(), nullable=False, comment='评论数量'),
    sa.Column('desc_detail', sa.String(length=100), nullable=False, comment='商品详情'),
    sa.Column('desc_pack', sa.String(length=100), nullable=False, comment='包装信息'),
    sa.Column('desc_server', sa.String(length=100), nullable=False, comment='售后服务'),
    sa.Column('ishot', sa.Boolean(), nullable=False, comment='是否在主页显示'),
    sa.Column('cid', sa.Integer(), nullable=False, comment='分类ID'),
    sa.Column('brand_id', sa.Integer(), nullable=False, comment='品牌ID'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('oauth_member_bind',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('client_type', sa.String(length=20), nullable=False),
    sa.Column('type', sa.Integer(), nullable=False),
    sa.Column('openid', sa.String(length=80), nullable=False),
    sa.Column('unionid', sa.String(length=100), nullable=False),
    sa.Column('session_key', sa.String(length=200), nullable=False, comment='会话秘钥'),
    sa.Column('extra', sa.Text(), nullable=False),
    sa.Column('member_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['member_id'], ['member.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('oauth_member_bind')
    op.drop_table('shopspu')
    op.drop_table('shopsku')
    op.drop_table('shopguigevalue')
    op.drop_table('shopguigekey')
    op.drop_table('shopguigeinfo')
    op.drop_table('shopdetailimage')
    op.drop_table('member')
    op.drop_table('category')
    op.drop_table('brank')
    op.drop_table('area')
    op.drop_table('AdminUser')
    # ### end Alembic commands ###
