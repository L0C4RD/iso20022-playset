from . import base_types
import RejectionStatus20Choice
import ConsentStatus4Choice
import PendingStatus20Choice

class ResponseStatus6Choice(base_types._BaseFieldType):

	__slots__ = ["_Rjctd", "_Cnsntd", "_Pdg"]
	@property
	def Rjctd(self):
		return self._Rjctd

	@Rjctd.setter
	def Rjctd(self, value):
		self._Rjctd = value if type(value) != auto else self.make_default("Rjctd")

	@Rjctd.deleter
	def Rjctd(self):
		del self._Rjctd
		self._Rjctd = None

	@property
	def Cnsntd(self):
		return self._Cnsntd

	@Cnsntd.setter
	def Cnsntd(self, value):
		self._Cnsntd = value if type(value) != auto else self.make_default("Cnsntd")

	@Cnsntd.deleter
	def Cnsntd(self):
		del self._Cnsntd
		self._Cnsntd = None

	@property
	def Pdg(self):
		return self._Pdg

	@Pdg.setter
	def Pdg(self, value):
		self._Pdg = value if type(value) != auto else self.make_default("Pdg")

	@Pdg.deleter
	def Pdg(self):
		del self._Pdg
		self._Pdg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rjctd', type=RejectionStatus20Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Cnsntd', type=ConsentStatus4Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Pdg', type=PendingStatus20Choice, min=0, max=1, mutex_group=1, array=False),
	))

