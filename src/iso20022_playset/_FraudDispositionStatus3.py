# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActionTaken2Code import ActionTaken2Code
from ._Max256Text import Max256Text

class FraudDispositionStatus3(base_types._BaseFieldType):

	__slots__ = ["_ActnTaken", "_ErrData", "_WrngData"]
	@property
	def ActnTaken(self):
		return self._ActnTaken

	@ActnTaken.setter
	def ActnTaken(self, value):
		self._ActnTaken = value if type(value) != base_types.auto else self.make_default("ActnTaken")

	@ActnTaken.deleter
	def ActnTaken(self):
		del self._ActnTaken
		self._ActnTaken = None

	@property
	def ErrData(self):
		return self._ErrData

	@ErrData.setter
	def ErrData(self, value):
		self._ErrData = value if type(value) != base_types.auto else self.make_default("ErrData")

	@ErrData.deleter
	def ErrData(self):
		del self._ErrData
		self._ErrData = None

	@property
	def WrngData(self):
		return self._WrngData

	@WrngData.setter
	def WrngData(self, value):
		self._WrngData = value if type(value) != base_types.auto else self.make_default("WrngData")

	@WrngData.deleter
	def WrngData(self):
		del self._WrngData
		self._WrngData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActnTaken', type=ActionTaken2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ErrData', type=Max256Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='WrngData', type=Max256Text, min=0, max=None, mutex_group=None, array=True),
	))