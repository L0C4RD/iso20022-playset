# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text

class TransportBySea4(base_types._BaseFieldType):

	__slots__ = ["_PortOfDschrge", "_PortOfLoadng", "_SeaCrrierNm", "_VsslNm"]
	@property
	def PortOfDschrge(self):
		return self._PortOfDschrge

	@PortOfDschrge.setter
	def PortOfDschrge(self, value):
		self._PortOfDschrge = value if value is not None else base_types.UninitialisedField(self, 'PortOfDschrge', Max35Text, False)

	@PortOfDschrge.deleter
	def PortOfDschrge(self):
		del self._PortOfDschrge
		self._PortOfDschrge = base_types.UninitialisedField(self, 'PortOfDschrge', Max35Text, False)

	@property
	def PortOfLoadng(self):
		return self._PortOfLoadng

	@PortOfLoadng.setter
	def PortOfLoadng(self, value):
		self._PortOfLoadng = value if value is not None else base_types.UninitialisedField(self, 'PortOfLoadng', Max35Text, False)

	@PortOfLoadng.deleter
	def PortOfLoadng(self):
		del self._PortOfLoadng
		self._PortOfLoadng = base_types.UninitialisedField(self, 'PortOfLoadng', Max35Text, False)

	@property
	def SeaCrrierNm(self):
		return self._SeaCrrierNm

	@SeaCrrierNm.setter
	def SeaCrrierNm(self, value):
		self._SeaCrrierNm = value if value is not None else base_types.UninitialisedField(self, 'SeaCrrierNm', Max35Text, False)

	@SeaCrrierNm.deleter
	def SeaCrrierNm(self):
		del self._SeaCrrierNm
		self._SeaCrrierNm = base_types.UninitialisedField(self, 'SeaCrrierNm', Max35Text, False)

	@property
	def VsslNm(self):
		return self._VsslNm

	@VsslNm.setter
	def VsslNm(self, value):
		self._VsslNm = value if value is not None else base_types.UninitialisedField(self, 'VsslNm', Max35Text, False)

	@VsslNm.deleter
	def VsslNm(self):
		del self._VsslNm
		self._VsslNm = base_types.UninitialisedField(self, 'VsslNm', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PortOfDschrge', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PortOfLoadng', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeaCrrierNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VsslNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))