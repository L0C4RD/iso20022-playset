# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CurrencyConversion36 import CurrencyConversion36
from ._GenericIdentification192 import GenericIdentification192
from ._Max35Text import Max35Text
from ._TransactionIdentifier1 import TransactionIdentifier1

class CardPaymentTransaction148(base_types._BaseFieldType):

	__slots__ = ["_CcyConvs", "_POIId", "_SaleRefId", "_TxId"]
	@property
	def CcyConvs(self):
		return self._CcyConvs

	@CcyConvs.setter
	def CcyConvs(self, value):
		self._CcyConvs = value if type(value) != base_types.auto else self.make_default("CcyConvs")

	@CcyConvs.deleter
	def CcyConvs(self):
		del self._CcyConvs
		self._CcyConvs = None

	@property
	def POIId(self):
		return self._POIId

	@POIId.setter
	def POIId(self, value):
		self._POIId = value if type(value) != base_types.auto else self.make_default("POIId")

	@POIId.deleter
	def POIId(self):
		del self._POIId
		self._POIId = None

	@property
	def SaleRefId(self):
		return self._SaleRefId

	@SaleRefId.setter
	def SaleRefId(self, value):
		self._SaleRefId = value if type(value) != base_types.auto else self.make_default("SaleRefId")

	@SaleRefId.deleter
	def SaleRefId(self):
		del self._SaleRefId
		self._SaleRefId = None

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if type(value) != base_types.auto else self.make_default("TxId")

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CcyConvs', type=CurrencyConversion36, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POIId', type=GenericIdentification192, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleRefId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TransactionIdentifier1, min=1, max=1, mutex_group=None, array=False),
	))