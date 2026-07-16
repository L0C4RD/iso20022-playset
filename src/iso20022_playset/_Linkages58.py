# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DocumentNumber5Choice
from . import References70Choice

class Linkages58(base_types._BaseFieldType):

	__slots__ = ["_MsgNb", "_Refs"]
	@property
	def MsgNb(self):
		return self._MsgNb

	@MsgNb.setter
	def MsgNb(self, value):
		self._MsgNb = value if value is not None else base_types.UninitialisedField(self, 'MsgNb', DocumentNumber5Choice, False)

	@MsgNb.deleter
	def MsgNb(self):
		del self._MsgNb
		self._MsgNb = base_types.UninitialisedField(self, 'MsgNb', DocumentNumber5Choice, False)

	@property
	def Refs(self):
		return self._Refs

	@Refs.setter
	def Refs(self, value):
		self._Refs = value if value is not None else base_types.UninitialisedField(self, 'Refs', References70Choice, False)

	@Refs.deleter
	def Refs(self):
		del self._Refs
		self._Refs = base_types.UninitialisedField(self, 'Refs', References70Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgNb', type=DocumentNumber5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Refs', type=References70Choice, min=1, max=1, mutex_group=None, array=False),
	))