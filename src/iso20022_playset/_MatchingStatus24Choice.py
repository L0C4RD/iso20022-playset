from . import base_types
from ._UnmatchedStatus16Choice import UnmatchedStatus16Choice
from ._ProprietaryReason4 import ProprietaryReason4
from ._ProprietaryStatusAndReason6 import ProprietaryStatusAndReason6

class MatchingStatus24Choice(base_types._BaseFieldType):

	__slots__ = ["_Umtchd", "_Mtchd", "_Prtry"]
	@property
	def Mtchd(self):
		return self._Mtchd

	@Mtchd.setter
	def Mtchd(self, value):
		self._Mtchd = value if type(value) != base_types.auto else self.make_default("Mtchd")

	@Mtchd.deleter
	def Mtchd(self):
		del self._Mtchd
		self._Mtchd = None

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if type(value) != base_types.auto else self.make_default("Prtry")

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = None

	@property
	def Umtchd(self):
		return self._Umtchd

	@Umtchd.setter
	def Umtchd(self, value):
		self._Umtchd = value if type(value) != base_types.auto else self.make_default("Umtchd")

	@Umtchd.deleter
	def Umtchd(self):
		del self._Umtchd
		self._Umtchd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Mtchd', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=ProprietaryStatusAndReason6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Umtchd', type=UnmatchedStatus16Choice, min=0, max=1, mutex_group=1, array=False),
	))

