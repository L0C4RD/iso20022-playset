# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max140Text
from . import MissingData1Choice

class UnableToApplyMissing2(base_types._BaseFieldType):

	__slots__ = ["_AddtlMssngInf", "_Tp"]
	@property
	def AddtlMssngInf(self):
		return self._AddtlMssngInf

	@AddtlMssngInf.setter
	def AddtlMssngInf(self, value):
		self._AddtlMssngInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlMssngInf', Max140Text, False)

	@AddtlMssngInf.deleter
	def AddtlMssngInf(self):
		del self._AddtlMssngInf
		self._AddtlMssngInf = base_types.UninitialisedField(self, 'AddtlMssngInf', Max140Text, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', MissingData1Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', MissingData1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlMssngInf', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=MissingData1Choice, min=1, max=1, mutex_group=None, array=False),
	))