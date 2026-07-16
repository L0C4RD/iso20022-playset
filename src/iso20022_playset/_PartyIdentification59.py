# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ClearingSystemIdentification2Choice
from . import LEIIdentifier
from . import Max105Text
from . import Max34Text
from . import PartyIdentification44

class PartyIdentification59(base_types._BaseFieldType):

	__slots__ = ["_AcctNb", "_Adr", "_AnyBIC", "_ClrSysId", "_LglNttyIdr", "_PtyNm"]
	@property
	def AcctNb(self):
		return self._AcctNb

	@AcctNb.setter
	def AcctNb(self, value):
		self._AcctNb = value if value is not None else base_types.UninitialisedField(self, 'AcctNb', Max34Text, False)

	@AcctNb.deleter
	def AcctNb(self):
		del self._AcctNb
		self._AcctNb = base_types.UninitialisedField(self, 'AcctNb', Max34Text, False)

	@property
	def Adr(self):
		return self._Adr

	@Adr.setter
	def Adr(self, value):
		self._Adr = value if value is not None else base_types.UninitialisedField(self, 'Adr', Max105Text, False)

	@Adr.deleter
	def Adr(self):
		del self._Adr
		self._Adr = base_types.UninitialisedField(self, 'Adr', Max105Text, False)

	@property
	def AnyBIC(self):
		return self._AnyBIC

	@AnyBIC.setter
	def AnyBIC(self, value):
		self._AnyBIC = value if value is not None else base_types.UninitialisedField(self, 'AnyBIC', PartyIdentification44, False)

	@AnyBIC.deleter
	def AnyBIC(self):
		del self._AnyBIC
		self._AnyBIC = base_types.UninitialisedField(self, 'AnyBIC', PartyIdentification44, False)

	@property
	def ClrSysId(self):
		return self._ClrSysId

	@ClrSysId.setter
	def ClrSysId(self, value):
		self._ClrSysId = value if value is not None else base_types.UninitialisedField(self, 'ClrSysId', ClearingSystemIdentification2Choice, False)

	@ClrSysId.deleter
	def ClrSysId(self):
		del self._ClrSysId
		self._ClrSysId = base_types.UninitialisedField(self, 'ClrSysId', ClearingSystemIdentification2Choice, False)

	@property
	def LglNttyIdr(self):
		return self._LglNttyIdr

	@LglNttyIdr.setter
	def LglNttyIdr(self, value):
		self._LglNttyIdr = value if value is not None else base_types.UninitialisedField(self, 'LglNttyIdr', LEIIdentifier, False)

	@LglNttyIdr.deleter
	def LglNttyIdr(self):
		del self._LglNttyIdr
		self._LglNttyIdr = base_types.UninitialisedField(self, 'LglNttyIdr', LEIIdentifier, False)

	@property
	def PtyNm(self):
		return self._PtyNm

	@PtyNm.setter
	def PtyNm(self, value):
		self._PtyNm = value if value is not None else base_types.UninitialisedField(self, 'PtyNm', Max34Text, False)

	@PtyNm.deleter
	def PtyNm(self):
		del self._PtyNm
		self._PtyNm = base_types.UninitialisedField(self, 'PtyNm', Max34Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctNb', type=Max34Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Adr', type=Max105Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AnyBIC', type=PartyIdentification44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrSysId', type=ClearingSystemIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LglNttyIdr', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyNm', type=Max34Text, min=0, max=1, mutex_group=None, array=False),
	))