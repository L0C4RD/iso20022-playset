from . import base_types
from .PortfolioIdentification3 import PortfolioIdentification3
from .NotApplicable1Code import NotApplicable1Code

class PortfolioCode5Choice(base_types._BaseFieldType):

	__slots__ = ["_Prtfl", "_NoPrtfl"]
	@property
	def Prtfl(self):
		return self._Prtfl

	@Prtfl.setter
	def Prtfl(self, value):
		self._Prtfl = value if type(value) != base_types.auto else self.make_default("Prtfl")

	@Prtfl.deleter
	def Prtfl(self):
		del self._Prtfl
		self._Prtfl = None

	@property
	def NoPrtfl(self):
		return self._NoPrtfl

	@NoPrtfl.setter
	def NoPrtfl(self, value):
		self._NoPrtfl = value if type(value) != base_types.auto else self.make_default("NoPrtfl")

	@NoPrtfl.deleter
	def NoPrtfl(self):
		del self._NoPrtfl
		self._NoPrtfl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Prtfl', type=PortfolioIdentification3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NoPrtfl', type=NotApplicable1Code, min=0, max=1, mutex_group=1, array=False),
	))

