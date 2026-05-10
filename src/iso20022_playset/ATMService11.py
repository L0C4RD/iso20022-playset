import base_types
import TrueFalseIndicator
import Max35Text
import ATMServiceType6Code

class ATMService11(base_types._BaseFieldType):

	__slots__ = ["_MultiAcct", "_ATMSvcCd", "_CshBck", "_SvcTp", "_SvcRef", "_SvcVarntId"]
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
	def CshBck(self):
		return self._CshBck

	@CshBck.setter
	def CshBck(self, value):
		self._CshBck = value if type(value) != auto else self.make_default("CshBck")

	@CshBck.deleter
	def CshBck(self):
		del self._CshBck
		self._CshBck = None

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
	def SvcVarntId(self):
		return self._SvcVarntId

	@SvcVarntId.setter
	def SvcVarntId(self, value):
		self._SvcVarntId = value if type(value) != auto else self.make_default("SvcVarntId")

	@SvcVarntId.deleter
	def SvcVarntId(self):
		del self._SvcVarntId
		self._SvcVarntId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MultiAcct', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ATMSvcCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshBck', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcTp', type=ATMServiceType6Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcVarntId', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
	))

