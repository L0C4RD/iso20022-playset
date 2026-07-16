# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODateTime
from . import Max35Text
from . import Party50Choice

class ReportHeader7(base_types._BaseFieldType):

	__slots__ = ["_CreDtTm", "_Fr", "_Id", "_To"]
	@property
	def CreDtTm(self):
		return self._CreDtTm

	@CreDtTm.setter
	def CreDtTm(self, value):
		self._CreDtTm = value if value is not None else base_types.UninitialisedField(self, 'CreDtTm', ISODateTime, False)

	@CreDtTm.deleter
	def CreDtTm(self):
		del self._CreDtTm
		self._CreDtTm = base_types.UninitialisedField(self, 'CreDtTm', ISODateTime, False)

	@property
	def Fr(self):
		return self._Fr

	@Fr.setter
	def Fr(self, value):
		self._Fr = value if value is not None else base_types.UninitialisedField(self, 'Fr', Party50Choice, False)

	@Fr.deleter
	def Fr(self):
		del self._Fr
		self._Fr = base_types.UninitialisedField(self, 'Fr', Party50Choice, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@property
	def To(self):
		return self._To

	@To.setter
	def To(self, value):
		self._To = value if value is not None else base_types.UninitialisedField(self, 'To', Party50Choice, False)

	@To.deleter
	def To(self):
		del self._To
		self._To = base_types.UninitialisedField(self, 'To', Party50Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Fr', type=Party50Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='To', type=Party50Choice, min=1, max=1, mutex_group=None, array=False),
	))