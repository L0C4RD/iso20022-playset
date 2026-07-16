# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import Percentage14Rate

class AdditionalRightThreshold2Choice(base_types._BaseFieldType):

	__slots__ = ["_AddtlRghtThrshld", "_AddtlRghtThrshldPctg"]
	@property
	def AddtlRghtThrshld(self):
		return self._AddtlRghtThrshld

	@AddtlRghtThrshld.setter
	def AddtlRghtThrshld(self, value):
		self._AddtlRghtThrshld = value if value is not None else base_types.UninitialisedField(self, 'AddtlRghtThrshld', Max35Text, False)

	@AddtlRghtThrshld.deleter
	def AddtlRghtThrshld(self):
		del self._AddtlRghtThrshld
		self._AddtlRghtThrshld = base_types.UninitialisedField(self, 'AddtlRghtThrshld', Max35Text, False)

	@property
	def AddtlRghtThrshldPctg(self):
		return self._AddtlRghtThrshldPctg

	@AddtlRghtThrshldPctg.setter
	def AddtlRghtThrshldPctg(self, value):
		self._AddtlRghtThrshldPctg = value if value is not None else base_types.UninitialisedField(self, 'AddtlRghtThrshldPctg', Percentage14Rate, False)

	@AddtlRghtThrshldPctg.deleter
	def AddtlRghtThrshldPctg(self):
		del self._AddtlRghtThrshldPctg
		self._AddtlRghtThrshldPctg = base_types.UninitialisedField(self, 'AddtlRghtThrshldPctg', Percentage14Rate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlRghtThrshld', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AddtlRghtThrshldPctg', type=Percentage14Rate, min=0, max=1, mutex_group=1, array=False),
	))