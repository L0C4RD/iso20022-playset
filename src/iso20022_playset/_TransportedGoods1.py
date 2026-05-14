# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DocumentIdentification7 import DocumentIdentification7
from ._Max70Text import Max70Text
from ._UserDefinedInformation1 import UserDefinedInformation1

class TransportedGoods1(base_types._BaseFieldType):

	__slots__ = ["_BuyrDfndInf", "_GoodsDesc", "_PurchsOrdrRef", "_SellrDfndInf"]
	@property
	def BuyrDfndInf(self):
		return self._BuyrDfndInf

	@BuyrDfndInf.setter
	def BuyrDfndInf(self, value):
		self._BuyrDfndInf = value if type(value) != base_types.auto else self.make_default("BuyrDfndInf")

	@BuyrDfndInf.deleter
	def BuyrDfndInf(self):
		del self._BuyrDfndInf
		self._BuyrDfndInf = None

	@property
	def GoodsDesc(self):
		return self._GoodsDesc

	@GoodsDesc.setter
	def GoodsDesc(self, value):
		self._GoodsDesc = value if type(value) != base_types.auto else self.make_default("GoodsDesc")

	@GoodsDesc.deleter
	def GoodsDesc(self):
		del self._GoodsDesc
		self._GoodsDesc = None

	@property
	def PurchsOrdrRef(self):
		return self._PurchsOrdrRef

	@PurchsOrdrRef.setter
	def PurchsOrdrRef(self, value):
		self._PurchsOrdrRef = value if type(value) != base_types.auto else self.make_default("PurchsOrdrRef")

	@PurchsOrdrRef.deleter
	def PurchsOrdrRef(self):
		del self._PurchsOrdrRef
		self._PurchsOrdrRef = None

	@property
	def SellrDfndInf(self):
		return self._SellrDfndInf

	@SellrDfndInf.setter
	def SellrDfndInf(self, value):
		self._SellrDfndInf = value if type(value) != base_types.auto else self.make_default("SellrDfndInf")

	@SellrDfndInf.deleter
	def SellrDfndInf(self):
		del self._SellrDfndInf
		self._SellrDfndInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BuyrDfndInf', type=UserDefinedInformation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='GoodsDesc', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PurchsOrdrRef', type=DocumentIdentification7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SellrDfndInf', type=UserDefinedInformation1, min=0, max=None, mutex_group=None, array=True),
	))