# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import IncorrectData1Choice
from . import Max140Text

class UnableToApplyIncorrect2(base_types._BaseFieldType):

	__slots__ = ["_AddtlIncrrctInf", "_Tp"]
	@property
	def AddtlIncrrctInf(self):
		return self._AddtlIncrrctInf

	@AddtlIncrrctInf.setter
	def AddtlIncrrctInf(self, value):
		self._AddtlIncrrctInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlIncrrctInf', Max140Text, False)

	@AddtlIncrrctInf.deleter
	def AddtlIncrrctInf(self):
		del self._AddtlIncrrctInf
		self._AddtlIncrrctInf = base_types.UninitialisedField(self, 'AddtlIncrrctInf', Max140Text, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', IncorrectData1Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', IncorrectData1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlIncrrctInf', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=IncorrectData1Choice, min=1, max=1, mutex_group=None, array=False),
	))