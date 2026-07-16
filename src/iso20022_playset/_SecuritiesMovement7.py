# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CollateralEntryType1Code
from . import FinancialInstrumentQuantity33Choice
from . import Max35Text
from . import SecurityIdentification19
from . import YesNoIndicator

class SecuritiesMovement7(base_types._BaseFieldType):

	__slots__ = ["_ClntSctiesMvmntId", "_CollMvmnt", "_FinInstrmId", "_Qty", "_SctiesMvmntTp", "_TrptyAgtSvcPrvdrSctiesMvmntId"]
	@property
	def ClntSctiesMvmntId(self):
		return self._ClntSctiesMvmntId

	@ClntSctiesMvmntId.setter
	def ClntSctiesMvmntId(self, value):
		self._ClntSctiesMvmntId = value if value is not None else base_types.UninitialisedField(self, 'ClntSctiesMvmntId', Max35Text, False)

	@ClntSctiesMvmntId.deleter
	def ClntSctiesMvmntId(self):
		del self._ClntSctiesMvmntId
		self._ClntSctiesMvmntId = base_types.UninitialisedField(self, 'ClntSctiesMvmntId', Max35Text, False)

	@property
	def CollMvmnt(self):
		return self._CollMvmnt

	@CollMvmnt.setter
	def CollMvmnt(self, value):
		self._CollMvmnt = value if value is not None else base_types.UninitialisedField(self, 'CollMvmnt', YesNoIndicator, False)

	@CollMvmnt.deleter
	def CollMvmnt(self):
		del self._CollMvmnt
		self._CollMvmnt = base_types.UninitialisedField(self, 'CollMvmnt', YesNoIndicator, False)

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification19, False)

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification19, False)

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if value is not None else base_types.UninitialisedField(self, 'Qty', FinancialInstrumentQuantity33Choice, False)

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = base_types.UninitialisedField(self, 'Qty', FinancialInstrumentQuantity33Choice, False)

	@property
	def SctiesMvmntTp(self):
		return self._SctiesMvmntTp

	@SctiesMvmntTp.setter
	def SctiesMvmntTp(self, value):
		self._SctiesMvmntTp = value if value is not None else base_types.UninitialisedField(self, 'SctiesMvmntTp', CollateralEntryType1Code, False)

	@SctiesMvmntTp.deleter
	def SctiesMvmntTp(self):
		del self._SctiesMvmntTp
		self._SctiesMvmntTp = base_types.UninitialisedField(self, 'SctiesMvmntTp', CollateralEntryType1Code, False)

	@property
	def TrptyAgtSvcPrvdrSctiesMvmntId(self):
		return self._TrptyAgtSvcPrvdrSctiesMvmntId

	@TrptyAgtSvcPrvdrSctiesMvmntId.setter
	def TrptyAgtSvcPrvdrSctiesMvmntId(self, value):
		self._TrptyAgtSvcPrvdrSctiesMvmntId = value if value is not None else base_types.UninitialisedField(self, 'TrptyAgtSvcPrvdrSctiesMvmntId', Max35Text, False)

	@TrptyAgtSvcPrvdrSctiesMvmntId.deleter
	def TrptyAgtSvcPrvdrSctiesMvmntId(self):
		del self._TrptyAgtSvcPrvdrSctiesMvmntId
		self._TrptyAgtSvcPrvdrSctiesMvmntId = base_types.UninitialisedField(self, 'TrptyAgtSvcPrvdrSctiesMvmntId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClntSctiesMvmntId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollMvmnt', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=FinancialInstrumentQuantity33Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesMvmntTp', type=CollateralEntryType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrptyAgtSvcPrvdrSctiesMvmntId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))