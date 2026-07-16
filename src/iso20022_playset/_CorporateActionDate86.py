# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateFormat30Choice

class CorporateActionDate86(base_types._BaseFieldType):

	__slots__ = ["_ExDvddDt", "_RcrdDt"]
	@property
	def ExDvddDt(self):
		return self._ExDvddDt

	@ExDvddDt.setter
	def ExDvddDt(self, value):
		self._ExDvddDt = value if value is not None else base_types.UninitialisedField(self, 'ExDvddDt', DateFormat30Choice, False)

	@ExDvddDt.deleter
	def ExDvddDt(self):
		del self._ExDvddDt
		self._ExDvddDt = base_types.UninitialisedField(self, 'ExDvddDt', DateFormat30Choice, False)

	@property
	def RcrdDt(self):
		return self._RcrdDt

	@RcrdDt.setter
	def RcrdDt(self, value):
		self._RcrdDt = value if value is not None else base_types.UninitialisedField(self, 'RcrdDt', DateFormat30Choice, False)

	@RcrdDt.deleter
	def RcrdDt(self):
		del self._RcrdDt
		self._RcrdDt = base_types.UninitialisedField(self, 'RcrdDt', DateFormat30Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ExDvddDt', type=DateFormat30Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcrdDt', type=DateFormat30Choice, min=0, max=1, mutex_group=None, array=False),
	))