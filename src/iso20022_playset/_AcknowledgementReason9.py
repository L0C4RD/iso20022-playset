# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcknowledgementReason12Choice
from . import Max210Text

class AcknowledgementReason9(base_types._BaseFieldType):

	__slots__ = ["_AddtlRsnInf", "_Cd"]
	@property
	def AddtlRsnInf(self):
		return self._AddtlRsnInf

	@AddtlRsnInf.setter
	def AddtlRsnInf(self, value):
		self._AddtlRsnInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlRsnInf', Max210Text, False)

	@AddtlRsnInf.deleter
	def AddtlRsnInf(self):
		del self._AddtlRsnInf
		self._AddtlRsnInf = base_types.UninitialisedField(self, 'AddtlRsnInf', Max210Text, False)

	@property
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if value is not None else base_types.UninitialisedField(self, 'Cd', AcknowledgementReason12Choice, False)

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = base_types.UninitialisedField(self, 'Cd', AcknowledgementReason12Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlRsnInf', type=Max210Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cd', type=AcknowledgementReason12Choice, min=1, max=1, mutex_group=None, array=False),
	))