# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import SpecialProgrammeDetails2

class SpecialProgrammeQualification2(base_types._BaseFieldType):

	__slots__ = ["_Dtl", "_Prgrmm"]
	@property
	def Dtl(self):
		return self._Dtl

	@Dtl.setter
	def Dtl(self, value):
		self._Dtl = value if value is not None else base_types.UninitialisedField(self, 'Dtl', SpecialProgrammeDetails2, True)

	@Dtl.deleter
	def Dtl(self):
		del self._Dtl
		self._Dtl = base_types.UninitialisedField(self, 'Dtl', SpecialProgrammeDetails2, True)

	@property
	def Prgrmm(self):
		return self._Prgrmm

	@Prgrmm.setter
	def Prgrmm(self, value):
		self._Prgrmm = value if value is not None else base_types.UninitialisedField(self, 'Prgrmm', Max35Text, False)

	@Prgrmm.deleter
	def Prgrmm(self):
		del self._Prgrmm
		self._Prgrmm = base_types.UninitialisedField(self, 'Prgrmm', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dtl', type=SpecialProgrammeDetails2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Prgrmm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))