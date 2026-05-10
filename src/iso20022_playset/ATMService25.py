from . import base_types
import ATMServiceType12Code
import Max35Text

class ATMService25(base_types._BaseFieldType):

	__slots__ = ["_SvcTp", "_SvcVarntId", "_ATMSvcCd", "_SvcRef"]
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
	def SvcRef(self):
		return self._SvcRef

	@SvcRef.setter
	def SvcRef(self, value):
		self._SvcRef = value if type(value) != auto else self.make_default("SvcRef")

	@SvcRef.deleter
	def SvcRef(self):
		del self._SvcRef
		self._SvcRef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SvcTp', type=ATMServiceType12Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcVarntId', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ATMSvcCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

