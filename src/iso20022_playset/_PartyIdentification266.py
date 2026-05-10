from . import base_types
from .ClearingSystemIdentification2Choice import ClearingSystemIdentification2Choice
from .PartyIdentification265 import PartyIdentification265
from .Max34Text import Max34Text
from .Max105Text import Max105Text
from .LEIIdentifier import LEIIdentifier

class PartyIdentification266(base_types._BaseFieldType):

	__slots__ = ["_Adr", "_PtyNm", "_ClrSysId", "_AnyBIC", "_LglNttyIdr", "_AcctNb"]
	@property
	def Adr(self):
		return self._Adr

	@Adr.setter
	def Adr(self, value):
		self._Adr = value if type(value) != base_types.auto else self.make_default("Adr")

	@Adr.deleter
	def Adr(self):
		del self._Adr
		self._Adr = None

	@property
	def PtyNm(self):
		return self._PtyNm

	@PtyNm.setter
	def PtyNm(self, value):
		self._PtyNm = value if type(value) != base_types.auto else self.make_default("PtyNm")

	@PtyNm.deleter
	def PtyNm(self):
		del self._PtyNm
		self._PtyNm = None

	@property
	def ClrSysId(self):
		return self._ClrSysId

	@ClrSysId.setter
	def ClrSysId(self, value):
		self._ClrSysId = value if type(value) != base_types.auto else self.make_default("ClrSysId")

	@ClrSysId.deleter
	def ClrSysId(self):
		del self._ClrSysId
		self._ClrSysId = None

	@property
	def AnyBIC(self):
		return self._AnyBIC

	@AnyBIC.setter
	def AnyBIC(self, value):
		self._AnyBIC = value if type(value) != base_types.auto else self.make_default("AnyBIC")

	@AnyBIC.deleter
	def AnyBIC(self):
		del self._AnyBIC
		self._AnyBIC = None

	@property
	def LglNttyIdr(self):
		return self._LglNttyIdr

	@LglNttyIdr.setter
	def LglNttyIdr(self, value):
		self._LglNttyIdr = value if type(value) != base_types.auto else self.make_default("LglNttyIdr")

	@LglNttyIdr.deleter
	def LglNttyIdr(self):
		del self._LglNttyIdr
		self._LglNttyIdr = None

	@property
	def AcctNb(self):
		return self._AcctNb

	@AcctNb.setter
	def AcctNb(self, value):
		self._AcctNb = value if type(value) != base_types.auto else self.make_default("AcctNb")

	@AcctNb.deleter
	def AcctNb(self):
		del self._AcctNb
		self._AcctNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Adr', type=Max105Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyNm', type=Max34Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrSysId', type=ClearingSystemIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AnyBIC', type=PartyIdentification265, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LglNttyIdr', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctNb', type=Max34Text, min=0, max=1, mutex_group=None, array=False),
	))

