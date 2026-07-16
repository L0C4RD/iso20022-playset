# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateFormat49Choice
from . import DateFormat67Choice

class CorporateActionDate109(base_types._BaseFieldType):

	__slots__ = ["_CoverXprtnDdln", "_TradgDt"]
	@property
	def CoverXprtnDdln(self):
		return self._CoverXprtnDdln

	@CoverXprtnDdln.setter
	def CoverXprtnDdln(self, value):
		self._CoverXprtnDdln = value if value is not None else base_types.UninitialisedField(self, 'CoverXprtnDdln', DateFormat67Choice, False)

	@CoverXprtnDdln.deleter
	def CoverXprtnDdln(self):
		del self._CoverXprtnDdln
		self._CoverXprtnDdln = base_types.UninitialisedField(self, 'CoverXprtnDdln', DateFormat67Choice, False)

	@property
	def TradgDt(self):
		return self._TradgDt

	@TradgDt.setter
	def TradgDt(self, value):
		self._TradgDt = value if value is not None else base_types.UninitialisedField(self, 'TradgDt', DateFormat49Choice, False)

	@TradgDt.deleter
	def TradgDt(self):
		del self._TradgDt
		self._TradgDt = base_types.UninitialisedField(self, 'TradgDt', DateFormat49Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CoverXprtnDdln', type=DateFormat67Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgDt', type=DateFormat49Choice, min=0, max=1, mutex_group=None, array=False),
	))