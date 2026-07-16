# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Amount2Choice

class Amount4Choice(base_types._BaseFieldType):

	__slots__ = ["_DcrAmt", "_IncrAmt"]
	@property
	def DcrAmt(self):
		return self._DcrAmt

	@DcrAmt.setter
	def DcrAmt(self, value):
		self._DcrAmt = value if value is not None else base_types.UninitialisedField(self, 'DcrAmt', Amount2Choice, False)

	@DcrAmt.deleter
	def DcrAmt(self):
		del self._DcrAmt
		self._DcrAmt = base_types.UninitialisedField(self, 'DcrAmt', Amount2Choice, False)

	@property
	def IncrAmt(self):
		return self._IncrAmt

	@IncrAmt.setter
	def IncrAmt(self, value):
		self._IncrAmt = value if value is not None else base_types.UninitialisedField(self, 'IncrAmt', Amount2Choice, False)

	@IncrAmt.deleter
	def IncrAmt(self):
		del self._IncrAmt
		self._IncrAmt = base_types.UninitialisedField(self, 'IncrAmt', Amount2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DcrAmt', type=Amount2Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IncrAmt', type=Amount2Choice, min=0, max=1, mutex_group=1, array=False),
	))