# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CountryCode
from . import Max35Text
from . import Max70Text

class TransportBySea6(base_types._BaseFieldType):

	__slots__ = ["_CrrierAgtCtry", "_CrrierAgtNm", "_PortOfDschrge", "_PortOfLoadng", "_SeaCrrierCtry", "_SeaCrrierNm", "_VsslNm"]
	@property
	def CrrierAgtCtry(self):
		return self._CrrierAgtCtry

	@CrrierAgtCtry.setter
	def CrrierAgtCtry(self, value):
		self._CrrierAgtCtry = value if value is not None else base_types.UninitialisedField(self, 'CrrierAgtCtry', CountryCode, False)

	@CrrierAgtCtry.deleter
	def CrrierAgtCtry(self):
		del self._CrrierAgtCtry
		self._CrrierAgtCtry = base_types.UninitialisedField(self, 'CrrierAgtCtry', CountryCode, False)

	@property
	def CrrierAgtNm(self):
		return self._CrrierAgtNm

	@CrrierAgtNm.setter
	def CrrierAgtNm(self, value):
		self._CrrierAgtNm = value if value is not None else base_types.UninitialisedField(self, 'CrrierAgtNm', Max70Text, False)

	@CrrierAgtNm.deleter
	def CrrierAgtNm(self):
		del self._CrrierAgtNm
		self._CrrierAgtNm = base_types.UninitialisedField(self, 'CrrierAgtNm', Max70Text, False)

	@property
	def PortOfDschrge(self):
		return self._PortOfDschrge

	@PortOfDschrge.setter
	def PortOfDschrge(self, value):
		self._PortOfDschrge = value if value is not None else base_types.UninitialisedField(self, 'PortOfDschrge', Max35Text, True)

	@PortOfDschrge.deleter
	def PortOfDschrge(self):
		del self._PortOfDschrge
		self._PortOfDschrge = base_types.UninitialisedField(self, 'PortOfDschrge', Max35Text, True)

	@property
	def PortOfLoadng(self):
		return self._PortOfLoadng

	@PortOfLoadng.setter
	def PortOfLoadng(self, value):
		self._PortOfLoadng = value if value is not None else base_types.UninitialisedField(self, 'PortOfLoadng', Max35Text, True)

	@PortOfLoadng.deleter
	def PortOfLoadng(self):
		del self._PortOfLoadng
		self._PortOfLoadng = base_types.UninitialisedField(self, 'PortOfLoadng', Max35Text, True)

	@property
	def SeaCrrierCtry(self):
		return self._SeaCrrierCtry

	@SeaCrrierCtry.setter
	def SeaCrrierCtry(self, value):
		self._SeaCrrierCtry = value if value is not None else base_types.UninitialisedField(self, 'SeaCrrierCtry', CountryCode, False)

	@SeaCrrierCtry.deleter
	def SeaCrrierCtry(self):
		del self._SeaCrrierCtry
		self._SeaCrrierCtry = base_types.UninitialisedField(self, 'SeaCrrierCtry', CountryCode, False)

	@property
	def SeaCrrierNm(self):
		return self._SeaCrrierNm

	@SeaCrrierNm.setter
	def SeaCrrierNm(self, value):
		self._SeaCrrierNm = value if value is not None else base_types.UninitialisedField(self, 'SeaCrrierNm', Max70Text, False)

	@SeaCrrierNm.deleter
	def SeaCrrierNm(self):
		del self._SeaCrrierNm
		self._SeaCrrierNm = base_types.UninitialisedField(self, 'SeaCrrierNm', Max70Text, False)

	@property
	def VsslNm(self):
		return self._VsslNm

	@VsslNm.setter
	def VsslNm(self, value):
		self._VsslNm = value if value is not None else base_types.UninitialisedField(self, 'VsslNm', Max70Text, False)

	@VsslNm.deleter
	def VsslNm(self):
		del self._VsslNm
		self._VsslNm = base_types.UninitialisedField(self, 'VsslNm', Max70Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CrrierAgtCtry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrrierAgtNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PortOfDschrge', type=Max35Text, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PortOfLoadng', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SeaCrrierCtry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeaCrrierNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VsslNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
	))