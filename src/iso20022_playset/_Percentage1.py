# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ExternalRelativeTo1Code
from . import PercentageRate

class Percentage1(base_types._BaseFieldType):

	__slots__ = ["_Rate", "_RltvTo"]
	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if value is not None else base_types.UninitialisedField(self, 'Rate', PercentageRate, False)

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = base_types.UninitialisedField(self, 'Rate', PercentageRate, False)

	@property
	def RltvTo(self):
		return self._RltvTo

	@RltvTo.setter
	def RltvTo(self, value):
		self._RltvTo = value if value is not None else base_types.UninitialisedField(self, 'RltvTo', ExternalRelativeTo1Code, False)

	@RltvTo.deleter
	def RltvTo(self):
		del self._RltvTo
		self._RltvTo = base_types.UninitialisedField(self, 'RltvTo', ExternalRelativeTo1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rate', type=PercentageRate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltvTo', type=ExternalRelativeTo1Code, min=1, max=1, mutex_group=None, array=False),
	))