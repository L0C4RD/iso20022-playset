# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import OnLinePIN11

class DeviceSecureInputResponse6(base_types._BaseFieldType):

	__slots__ = ["_CrdhldrPIN"]
	@property
	def CrdhldrPIN(self):
		return self._CrdhldrPIN

	@CrdhldrPIN.setter
	def CrdhldrPIN(self, value):
		self._CrdhldrPIN = value if value is not None else base_types.UninitialisedField(self, 'CrdhldrPIN', OnLinePIN11, False)

	@CrdhldrPIN.deleter
	def CrdhldrPIN(self):
		del self._CrdhldrPIN
		self._CrdhldrPIN = base_types.UninitialisedField(self, 'CrdhldrPIN', OnLinePIN11, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CrdhldrPIN', type=OnLinePIN11, min=0, max=1, mutex_group=None, array=False),
	))