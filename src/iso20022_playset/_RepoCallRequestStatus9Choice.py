from . import base_types
from .ProprietaryStatusAndReason7 import ProprietaryStatusAndReason7
from .DeniedStatus18Choice import DeniedStatus18Choice
from .AcknowledgedAcceptedStatus27Choice import AcknowledgedAcceptedStatus27Choice

class RepoCallRequestStatus9Choice(base_types._BaseFieldType):

	__slots__ = ["_Dnd", "_Prtry", "_AckdAccptd"]
	@property
	def Dnd(self):
		return self._Dnd

	@Dnd.setter
	def Dnd(self, value):
		self._Dnd = value if type(value) != base_types.auto else self.make_default("Dnd")

	@Dnd.deleter
	def Dnd(self):
		del self._Dnd
		self._Dnd = None

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
	def AckdAccptd(self):
		return self._AckdAccptd

	@AckdAccptd.setter
	def AckdAccptd(self, value):
		self._AckdAccptd = value if type(value) != base_types.auto else self.make_default("AckdAccptd")

	@AckdAccptd.deleter
	def AckdAccptd(self):
		del self._AckdAccptd
		self._AckdAccptd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dnd', type=DeniedStatus18Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=ProprietaryStatusAndReason7, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AckdAccptd', type=AcknowledgedAcceptedStatus27Choice, min=0, max=1, mutex_group=1, array=False),
	))

