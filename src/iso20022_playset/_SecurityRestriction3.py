from . import base_types
from ._DateTimePeriod2 import DateTimePeriod2
from ._InvestorRestrictionType3Choice import InvestorRestrictionType3Choice
from ._InvestorType3Choice import InvestorType3Choice
from ._LegalRestrictions5Choice import LegalRestrictions5Choice
from ._SecurityRestrictionType2Choice import SecurityRestrictionType2Choice

class SecurityRestriction3(base_types._BaseFieldType):

	__slots__ = ["_FctvPrd", "_InvstrRstrctnTp", "_InvstrTp", "_LglRstrctnTp", "_RstrctnTp"]
	@property
	def FctvPrd(self):
		return self._FctvPrd

	@FctvPrd.setter
	def FctvPrd(self, value):
		self._FctvPrd = value if type(value) != base_types.auto else self.make_default("FctvPrd")

	@FctvPrd.deleter
	def FctvPrd(self):
		del self._FctvPrd
		self._FctvPrd = None

	@property
	def InvstrRstrctnTp(self):
		return self._InvstrRstrctnTp

	@InvstrRstrctnTp.setter
	def InvstrRstrctnTp(self, value):
		self._InvstrRstrctnTp = value if type(value) != base_types.auto else self.make_default("InvstrRstrctnTp")

	@InvstrRstrctnTp.deleter
	def InvstrRstrctnTp(self):
		del self._InvstrRstrctnTp
		self._InvstrRstrctnTp = None

	@property
	def InvstrTp(self):
		return self._InvstrTp

	@InvstrTp.setter
	def InvstrTp(self, value):
		self._InvstrTp = value if type(value) != base_types.auto else self.make_default("InvstrTp")

	@InvstrTp.deleter
	def InvstrTp(self):
		del self._InvstrTp
		self._InvstrTp = None

	@property
	def LglRstrctnTp(self):
		return self._LglRstrctnTp

	@LglRstrctnTp.setter
	def LglRstrctnTp(self, value):
		self._LglRstrctnTp = value if type(value) != base_types.auto else self.make_default("LglRstrctnTp")

	@LglRstrctnTp.deleter
	def LglRstrctnTp(self):
		del self._LglRstrctnTp
		self._LglRstrctnTp = None

	@property
	def RstrctnTp(self):
		return self._RstrctnTp

	@RstrctnTp.setter
	def RstrctnTp(self, value):
		self._RstrctnTp = value if type(value) != base_types.auto else self.make_default("RstrctnTp")

	@RstrctnTp.deleter
	def RstrctnTp(self):
		del self._RstrctnTp
		self._RstrctnTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FctvPrd', type=DateTimePeriod2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstrRstrctnTp', type=InvestorRestrictionType3Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InvstrTp', type=InvestorType3Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LglRstrctnTp', type=LegalRestrictions5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RstrctnTp', type=SecurityRestrictionType2Choice, min=0, max=1, mutex_group=None, array=False),
	))

