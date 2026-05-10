from . import base_types
from .VerificationReason1Choice import VerificationReason1Choice
from .IdentificationVerificationIndicator import IdentificationVerificationIndicator
from .IdentificationInformation5 import IdentificationInformation5
from .Max35Text import Max35Text

class VerificationReport5(base_types._BaseFieldType):

	__slots__ = ["_OrgnlPtyAndAcctId", "_Vrfctn", "_UpdtdPtyAndAcctId", "_Rsn", "_OrgnlId"]
	@property
	def OrgnlPtyAndAcctId(self):
		return self._OrgnlPtyAndAcctId

	@OrgnlPtyAndAcctId.setter
	def OrgnlPtyAndAcctId(self, value):
		self._OrgnlPtyAndAcctId = value if type(value) != base_types.auto else self.make_default("OrgnlPtyAndAcctId")

	@OrgnlPtyAndAcctId.deleter
	def OrgnlPtyAndAcctId(self):
		del self._OrgnlPtyAndAcctId
		self._OrgnlPtyAndAcctId = None

	@property
	def Vrfctn(self):
		return self._Vrfctn

	@Vrfctn.setter
	def Vrfctn(self, value):
		self._Vrfctn = value if type(value) != base_types.auto else self.make_default("Vrfctn")

	@Vrfctn.deleter
	def Vrfctn(self):
		del self._Vrfctn
		self._Vrfctn = None

	@property
	def UpdtdPtyAndAcctId(self):
		return self._UpdtdPtyAndAcctId

	@UpdtdPtyAndAcctId.setter
	def UpdtdPtyAndAcctId(self, value):
		self._UpdtdPtyAndAcctId = value if type(value) != base_types.auto else self.make_default("UpdtdPtyAndAcctId")

	@UpdtdPtyAndAcctId.deleter
	def UpdtdPtyAndAcctId(self):
		del self._UpdtdPtyAndAcctId
		self._UpdtdPtyAndAcctId = None

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if type(value) != base_types.auto else self.make_default("Rsn")

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = None

	@property
	def OrgnlId(self):
		return self._OrgnlId

	@OrgnlId.setter
	def OrgnlId(self, value):
		self._OrgnlId = value if type(value) != base_types.auto else self.make_default("OrgnlId")

	@OrgnlId.deleter
	def OrgnlId(self):
		del self._OrgnlId
		self._OrgnlId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlPtyAndAcctId', type=IdentificationInformation5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrfctn', type=IdentificationVerificationIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UpdtdPtyAndAcctId', type=IdentificationInformation5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=VerificationReason1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

