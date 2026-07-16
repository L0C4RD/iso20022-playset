# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate

class UpdateLogDate1(base_types._BaseFieldType):

	__slots__ = ["_New", "_Od"]
	@property
	def New(self):
		return self._New

	@New.setter
	def New(self, value):
		self._New = value if value is not None else base_types.UninitialisedField(self, 'New', ISODate, False)

	@New.deleter
	def New(self):
		del self._New
		self._New = base_types.UninitialisedField(self, 'New', ISODate, False)

	@property
	def Od(self):
		return self._Od

	@Od.setter
	def Od(self, value):
		self._Od = value if value is not None else base_types.UninitialisedField(self, 'Od', ISODate, False)

	@Od.deleter
	def Od(self):
		del self._Od
		self._Od = base_types.UninitialisedField(self, 'Od', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='New', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Od', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))