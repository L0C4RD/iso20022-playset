import base_types
import Max52Text
import NotApplicable1Code

class PortfolioCode3Choice(base_types._BaseFieldType):

	__slots__ = ["_NoPrtfl", "_Cd"]
	@property
	def NoPrtfl(self):
		return self._NoPrtfl

	@NoPrtfl.setter
	def NoPrtfl(self, value):
		self._NoPrtfl = value if type(value) != auto else self.make_default("NoPrtfl")

	@NoPrtfl.deleter
	def NoPrtfl(self):
		del self._NoPrtfl
		self._NoPrtfl = None

	@property
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if type(value) != auto else self.make_default("Cd")

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NoPrtfl', type=NotApplicable1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Cd', type=Max52Text, min=0, max=1, mutex_group=1, array=False),
	))

