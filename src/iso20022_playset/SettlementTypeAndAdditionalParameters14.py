from . import base_types
import ReceiveDelivery1Code
import YesNoIndicator
import Max35Text
import DeliveryReceiptType2Code

class SettlementTypeAndAdditionalParameters14(base_types._BaseFieldType):

	__slots__ = ["_SctiesMvmntTp", "_Pmt", "_CorpActnEvtId", "_CmonId", "_RcncltnInd"]
	@property
	def SctiesMvmntTp(self):
		return self._SctiesMvmntTp

	@SctiesMvmntTp.setter
	def SctiesMvmntTp(self, value):
		self._SctiesMvmntTp = value if type(value) != auto else self.make_default("SctiesMvmntTp")

	@SctiesMvmntTp.deleter
	def SctiesMvmntTp(self):
		del self._SctiesMvmntTp
		self._SctiesMvmntTp = None

	@property
	def Pmt(self):
		return self._Pmt

	@Pmt.setter
	def Pmt(self, value):
		self._Pmt = value if type(value) != auto else self.make_default("Pmt")

	@Pmt.deleter
	def Pmt(self):
		del self._Pmt
		self._Pmt = None

	@property
	def CorpActnEvtId(self):
		return self._CorpActnEvtId

	@CorpActnEvtId.setter
	def CorpActnEvtId(self, value):
		self._CorpActnEvtId = value if type(value) != auto else self.make_default("CorpActnEvtId")

	@CorpActnEvtId.deleter
	def CorpActnEvtId(self):
		del self._CorpActnEvtId
		self._CorpActnEvtId = None

	@property
	def CmonId(self):
		return self._CmonId

	@CmonId.setter
	def CmonId(self, value):
		self._CmonId = value if type(value) != auto else self.make_default("CmonId")

	@CmonId.deleter
	def CmonId(self):
		del self._CmonId
		self._CmonId = None

	@property
	def RcncltnInd(self):
		return self._RcncltnInd

	@RcncltnInd.setter
	def RcncltnInd(self, value):
		self._RcncltnInd = value if type(value) != auto else self.make_default("RcncltnInd")

	@RcncltnInd.deleter
	def RcncltnInd(self):
		del self._RcncltnInd
		self._RcncltnInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SctiesMvmntTp', type=ReceiveDelivery1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pmt', type=DeliveryReceiptType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnEvtId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmonId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
	))

