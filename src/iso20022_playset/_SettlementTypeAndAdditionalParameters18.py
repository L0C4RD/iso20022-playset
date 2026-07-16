# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DeliveryReceiptType2Code
from . import ReceiveDelivery1Code
from . import RestrictedFINXMax16Text
from . import YesNoIndicator

class SettlementTypeAndAdditionalParameters18(base_types._BaseFieldType):

	__slots__ = ["_CmonId", "_CorpActnEvtId", "_Pmt", "_RcncltnInd", "_SctiesMvmntTp"]
	@property
	def CmonId(self):
		return self._CmonId

	@CmonId.setter
	def CmonId(self, value):
		self._CmonId = value if value is not None else base_types.UninitialisedField(self, 'CmonId', RestrictedFINXMax16Text, False)

	@CmonId.deleter
	def CmonId(self):
		del self._CmonId
		self._CmonId = base_types.UninitialisedField(self, 'CmonId', RestrictedFINXMax16Text, False)

	@property
	def CorpActnEvtId(self):
		return self._CorpActnEvtId

	@CorpActnEvtId.setter
	def CorpActnEvtId(self, value):
		self._CorpActnEvtId = value if value is not None else base_types.UninitialisedField(self, 'CorpActnEvtId', RestrictedFINXMax16Text, False)

	@CorpActnEvtId.deleter
	def CorpActnEvtId(self):
		del self._CorpActnEvtId
		self._CorpActnEvtId = base_types.UninitialisedField(self, 'CorpActnEvtId', RestrictedFINXMax16Text, False)

	@property
	def Pmt(self):
		return self._Pmt

	@Pmt.setter
	def Pmt(self, value):
		self._Pmt = value if value is not None else base_types.UninitialisedField(self, 'Pmt', DeliveryReceiptType2Code, False)

	@Pmt.deleter
	def Pmt(self):
		del self._Pmt
		self._Pmt = base_types.UninitialisedField(self, 'Pmt', DeliveryReceiptType2Code, False)

	@property
	def RcncltnInd(self):
		return self._RcncltnInd

	@RcncltnInd.setter
	def RcncltnInd(self, value):
		self._RcncltnInd = value if value is not None else base_types.UninitialisedField(self, 'RcncltnInd', YesNoIndicator, False)

	@RcncltnInd.deleter
	def RcncltnInd(self):
		del self._RcncltnInd
		self._RcncltnInd = base_types.UninitialisedField(self, 'RcncltnInd', YesNoIndicator, False)

	@property
	def SctiesMvmntTp(self):
		return self._SctiesMvmntTp

	@SctiesMvmntTp.setter
	def SctiesMvmntTp(self, value):
		self._SctiesMvmntTp = value if value is not None else base_types.UninitialisedField(self, 'SctiesMvmntTp', ReceiveDelivery1Code, False)

	@SctiesMvmntTp.deleter
	def SctiesMvmntTp(self):
		del self._SctiesMvmntTp
		self._SctiesMvmntTp = base_types.UninitialisedField(self, 'SctiesMvmntTp', ReceiveDelivery1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CmonId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnEvtId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pmt', type=DeliveryReceiptType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesMvmntTp', type=ReceiveDelivery1Code, min=0, max=1, mutex_group=None, array=False),
	))