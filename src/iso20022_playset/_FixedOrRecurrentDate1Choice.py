# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DateInformation1 import DateInformation1
from ._ISODate import ISODate

class FixedOrRecurrentDate1Choice(base_types._BaseFieldType):

	__slots__ = ["_FxdDt", "_RcrntDt"]
	@property
	def FxdDt(self):
		return self._FxdDt

	@FxdDt.setter
	def FxdDt(self, value):
		self._FxdDt = value if type(value) != base_types.auto else self.make_default("FxdDt")

	@FxdDt.deleter
	def FxdDt(self):
		del self._FxdDt
		self._FxdDt = None

	@property
	def RcrntDt(self):
		return self._RcrntDt

	@RcrntDt.setter
	def RcrntDt(self, value):
		self._RcrntDt = value if type(value) != base_types.auto else self.make_default("RcrntDt")

	@RcrntDt.deleter
	def RcrntDt(self):
		del self._RcrntDt
		self._RcrntDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FxdDt', type=ISODate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RcrntDt', type=DateInformation1, min=0, max=1, mutex_group=1, array=False),
	))