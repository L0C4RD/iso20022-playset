# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max52Text
from . import NotApplicable1Code

class PortfolioCode3Choice(base_types._BaseFieldType):

	__slots__ = ["_Cd", "_NoPrtfl"]
	@property
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if value is not None else base_types.UninitialisedField(self, 'Cd', Max52Text, False)

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = base_types.UninitialisedField(self, 'Cd', Max52Text, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cd', type=Max52Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NoPrtfl', type=NotApplicable1Code, min=0, max=1, mutex_group=1, array=False),
	))