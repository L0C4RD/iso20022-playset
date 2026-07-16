# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountOrRate3Choice
from . import CommissionType5Choice

class Commission21(base_types._BaseFieldType):

	__slots__ = ["_ComssnApld", "_ComssnTp"]
	@property
	def ComssnApld(self):
		return self._ComssnApld

	@ComssnApld.setter
	def ComssnApld(self, value):
		self._ComssnApld = value if value is not None else base_types.UninitialisedField(self, 'ComssnApld', AmountOrRate3Choice, False)

	@ComssnApld.deleter
	def ComssnApld(self):
		del self._ComssnApld
		self._ComssnApld = base_types.UninitialisedField(self, 'ComssnApld', AmountOrRate3Choice, False)

	@property
	def ComssnTp(self):
		return self._ComssnTp

	@ComssnTp.setter
	def ComssnTp(self, value):
		self._ComssnTp = value if value is not None else base_types.UninitialisedField(self, 'ComssnTp', CommissionType5Choice, False)

	@ComssnTp.deleter
	def ComssnTp(self):
		del self._ComssnTp
		self._ComssnTp = base_types.UninitialisedField(self, 'ComssnTp', CommissionType5Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ComssnApld', type=AmountOrRate3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ComssnTp', type=CommissionType5Choice, min=1, max=1, mutex_group=None, array=False),
	))