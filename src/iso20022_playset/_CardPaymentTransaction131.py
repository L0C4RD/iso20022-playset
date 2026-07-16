# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CurrencyConversion31
from . import GenericIdentification32
from . import Max35Text
from . import TransactionIdentifier1

class CardPaymentTransaction131(base_types._BaseFieldType):

	__slots__ = ["_CcyConvs", "_POIId", "_SaleRefId", "_TxId"]
	@property
	def CcyConvs(self):
		return self._CcyConvs

	@CcyConvs.setter
	def CcyConvs(self, value):
		self._CcyConvs = value if value is not None else base_types.UninitialisedField(self, 'CcyConvs', CurrencyConversion31, False)

	@CcyConvs.deleter
	def CcyConvs(self):
		del self._CcyConvs
		self._CcyConvs = base_types.UninitialisedField(self, 'CcyConvs', CurrencyConversion31, False)

	@property
	def POIId(self):
		return self._POIId

	@POIId.setter
	def POIId(self, value):
		self._POIId = value if value is not None else base_types.UninitialisedField(self, 'POIId', GenericIdentification32, False)

	@POIId.deleter
	def POIId(self):
		del self._POIId
		self._POIId = base_types.UninitialisedField(self, 'POIId', GenericIdentification32, False)

	@property
	def SaleRefId(self):
		return self._SaleRefId

	@SaleRefId.setter
	def SaleRefId(self, value):
		self._SaleRefId = value if value is not None else base_types.UninitialisedField(self, 'SaleRefId', Max35Text, False)

	@SaleRefId.deleter
	def SaleRefId(self):
		del self._SaleRefId
		self._SaleRefId = base_types.UninitialisedField(self, 'SaleRefId', Max35Text, False)

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if value is not None else base_types.UninitialisedField(self, 'TxId', TransactionIdentifier1, False)

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = base_types.UninitialisedField(self, 'TxId', TransactionIdentifier1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CcyConvs', type=CurrencyConversion31, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POIId', type=GenericIdentification32, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleRefId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TransactionIdentifier1, min=1, max=1, mutex_group=None, array=False),
	))