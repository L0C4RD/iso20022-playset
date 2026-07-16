# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import TechnicalIdentification2Choice

class UpdateLogTechnicalAddress1(base_types._BaseFieldType):

	__slots__ = ["_New", "_Od"]
	@property
	def New(self):
		return self._New

	@New.setter
	def New(self, value):
		self._New = value if value is not None else base_types.UninitialisedField(self, 'New', TechnicalIdentification2Choice, False)

	@New.deleter
	def New(self):
		del self._New
		self._New = base_types.UninitialisedField(self, 'New', TechnicalIdentification2Choice, False)

	@property
	def Od(self):
		return self._Od

	@Od.setter
	def Od(self, value):
		self._Od = value if value is not None else base_types.UninitialisedField(self, 'Od', TechnicalIdentification2Choice, False)

	@Od.deleter
	def Od(self):
		del self._Od
		self._Od = base_types.UninitialisedField(self, 'Od', TechnicalIdentification2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='New', type=TechnicalIdentification2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Od', type=TechnicalIdentification2Choice, min=1, max=1, mutex_group=None, array=False),
	))