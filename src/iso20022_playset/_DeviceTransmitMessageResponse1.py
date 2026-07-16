# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max100KBinary

class DeviceTransmitMessageResponse1(base_types._BaseFieldType):

	__slots__ = ["_RcvdMsg"]
	@property
	def RcvdMsg(self):
		return self._RcvdMsg

	@RcvdMsg.setter
	def RcvdMsg(self, value):
		self._RcvdMsg = value if value is not None else base_types.UninitialisedField(self, 'RcvdMsg', Max100KBinary, False)

	@RcvdMsg.deleter
	def RcvdMsg(self):
		del self._RcvdMsg
		self._RcvdMsg = base_types.UninitialisedField(self, 'RcvdMsg', Max100KBinary, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='RcvdMsg', type=Max100KBinary, min=0, max=1, mutex_group=None, array=False),
	))