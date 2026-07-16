# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import NotApplicable1Code
from . import PortfolioIdentification3

class PortfolioCode5Choice(base_types._BaseFieldType):

	__slots__ = ["_NoPrtfl", "_Prtfl"]
	@property
	def NoPrtfl(self):
		return self._NoPrtfl

	@NoPrtfl.setter
	def NoPrtfl(self, value):
		self._NoPrtfl = value if value is not None else base_types.UninitialisedField(self, 'NoPrtfl', NotApplicable1Code, False)

	@NoPrtfl.deleter
	def NoPrtfl(self):
		del self._NoPrtfl
		self._NoPrtfl = base_types.UninitialisedField(self, 'NoPrtfl', NotApplicable1Code, False)

	@property
	def Prtfl(self):
		return self._Prtfl

	@Prtfl.setter
	def Prtfl(self, value):
		self._Prtfl = value if value is not None else base_types.UninitialisedField(self, 'Prtfl', PortfolioIdentification3, False)

	@Prtfl.deleter
	def Prtfl(self):
		del self._Prtfl
		self._Prtfl = base_types.UninitialisedField(self, 'Prtfl', PortfolioIdentification3, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NoPrtfl', type=NotApplicable1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtfl', type=PortfolioIdentification3, min=0, max=1, mutex_group=1, array=False),
	))