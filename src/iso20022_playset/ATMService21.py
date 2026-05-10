from . import base_types
from .ATMServiceType5Code import ATMServiceType5Code
from .Max35Text import Max35Text

class ATMService21(base_types._BaseFieldType):

	__slots__ = ["_ATMSvcCd", "_HstSvcCd", "_SvcVarntId", "_SvcTp", "_SvcRef"]
	@property
	def ATMSvcCd(self):
		return self._ATMSvcCd

	@ATMSvcCd.setter
	def ATMSvcCd(self, value):
		self._ATMSvcCd = value if type(value) != base_types.auto else self.make_default("ATMSvcCd")

	@ATMSvcCd.deleter
	def ATMSvcCd(self):
		del self._ATMSvcCd
		self._ATMSvcCd = None

	@property
	def HstSvcCd(self):
		return self._HstSvcCd

	@HstSvcCd.setter
	def HstSvcCd(self, value):
		self._HstSvcCd = value if type(value) != base_types.auto else self.make_default("HstSvcCd")

	@HstSvcCd.deleter
	def HstSvcCd(self):
		del self._HstSvcCd
		self._HstSvcCd = None

	@property
	def SvcVarntId(self):
		return self._SvcVarntId

	@SvcVarntId.setter
	def SvcVarntId(self, value):
		self._SvcVarntId = value if type(value) != base_types.auto else self.make_default("SvcVarntId")

	@SvcVarntId.deleter
	def SvcVarntId(self):
		del self._SvcVarntId
		self._SvcVarntId = None

	@property
	def SvcTp(self):
		return self._SvcTp

	@SvcTp.setter
	def SvcTp(self, value):
		self._SvcTp = value if type(value) != base_types.auto else self.make_default("SvcTp")

	@SvcTp.deleter
	def SvcTp(self):
		del self._SvcTp
		self._SvcTp = None

	@property
	def SvcRef(self):
		return self._SvcRef

	@SvcRef.setter
	def SvcRef(self, value):
		self._SvcRef = value if type(value) != base_types.auto else self.make_default("SvcRef")

	@SvcRef.deleter
	def SvcRef(self):
		del self._SvcRef
		self._SvcRef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ATMSvcCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HstSvcCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcVarntId', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SvcTp', type=ATMServiceType5Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

