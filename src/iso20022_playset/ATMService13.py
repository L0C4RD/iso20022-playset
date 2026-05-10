from . import base_types
from .Max35Text import Max35Text
from .ATMServiceType6Code import ATMServiceType6Code
from .TrueFalseIndicator import TrueFalseIndicator

class ATMService13(base_types._BaseFieldType):

	__slots__ = ["_MultiAcct", "_SvcRef", "_HstSvcCd", "_ATMSvcCd", "_SvcTp", "_PrtlDpst", "_SvcVarntId", "_CshBck"]
	@property
	def MultiAcct(self):
		return self._MultiAcct

	@MultiAcct.setter
	def MultiAcct(self, value):
		self._MultiAcct = value if type(value) != auto else self.make_default("MultiAcct")

	@MultiAcct.deleter
	def MultiAcct(self):
		del self._MultiAcct
		self._MultiAcct = None

	@property
	def SvcRef(self):
		return self._SvcRef

	@SvcRef.setter
	def SvcRef(self, value):
		self._SvcRef = value if type(value) != auto else self.make_default("SvcRef")

	@SvcRef.deleter
	def SvcRef(self):
		del self._SvcRef
		self._SvcRef = None

	@property
	def HstSvcCd(self):
		return self._HstSvcCd

	@HstSvcCd.setter
	def HstSvcCd(self, value):
		self._HstSvcCd = value if type(value) != auto else self.make_default("HstSvcCd")

	@HstSvcCd.deleter
	def HstSvcCd(self):
		del self._HstSvcCd
		self._HstSvcCd = None

	@property
	def ATMSvcCd(self):
		return self._ATMSvcCd

	@ATMSvcCd.setter
	def ATMSvcCd(self, value):
		self._ATMSvcCd = value if type(value) != auto else self.make_default("ATMSvcCd")

	@ATMSvcCd.deleter
	def ATMSvcCd(self):
		del self._ATMSvcCd
		self._ATMSvcCd = None

	@property
	def SvcTp(self):
		return self._SvcTp

	@SvcTp.setter
	def SvcTp(self, value):
		self._SvcTp = value if type(value) != auto else self.make_default("SvcTp")

	@SvcTp.deleter
	def SvcTp(self):
		del self._SvcTp
		self._SvcTp = None

	@property
	def PrtlDpst(self):
		return self._PrtlDpst

	@PrtlDpst.setter
	def PrtlDpst(self, value):
		self._PrtlDpst = value if type(value) != auto else self.make_default("PrtlDpst")

	@PrtlDpst.deleter
	def PrtlDpst(self):
		del self._PrtlDpst
		self._PrtlDpst = None

	@property
	def SvcVarntId(self):
		return self._SvcVarntId

	@SvcVarntId.setter
	def SvcVarntId(self, value):
		self._SvcVarntId = value if type(value) != auto else self.make_default("SvcVarntId")

	@SvcVarntId.deleter
	def SvcVarntId(self):
		del self._SvcVarntId
		self._SvcVarntId = None

	@property
	def CshBck(self):
		return self._CshBck

	@CshBck.setter
	def CshBck(self, value):
		self._CshBck = value if type(value) != auto else self.make_default("CshBck")

	@CshBck.deleter
	def CshBck(self):
		del self._CshBck
		self._CshBck = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MultiAcct', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HstSvcCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ATMSvcCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcTp', type=ATMServiceType6Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtlDpst', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcVarntId', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CshBck', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))

