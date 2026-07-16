# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Amount1Choice
from . import Max2000Text

class UndertakingAmount2(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_AmtChc"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max2000Text, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max2000Text, True)

	@property
	def AmtChc(self):
		return self._AmtChc

	@AmtChc.setter
	def AmtChc(self, value):
		self._AmtChc = value if value is not None else base_types.UninitialisedField(self, 'AmtChc', Amount1Choice, False)

	@AmtChc.deleter
	def AmtChc(self):
		del self._AmtChc
		self._AmtChc = base_types.UninitialisedField(self, 'AmtChc', Amount1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='AmtChc', type=Amount1Choice, min=1, max=1, mutex_group=None, array=False),
	))