# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CountryCode
from . import Exact7NumericText
from . import Max35Text
from . import Max70Text

class TransportBySea5(base_types._BaseFieldType):

	__slots__ = ["_ChrtrrNm", "_CrrierAgtCtry", "_CrrierAgtNm", "_IMONb", "_MstrNm", "_OwnrNm", "_PortOfDschrge", "_PortOfLoadng", "_SeaCrrierCtry", "_SeaCrrierNm", "_VsslNm", "_VygNb"]
	@property
	def ChrtrrNm(self):
		return self._ChrtrrNm

	@ChrtrrNm.setter
	def ChrtrrNm(self, value):
		self._ChrtrrNm = value if value is not None else base_types.UninitialisedField(self, 'ChrtrrNm', Max70Text, False)

	@ChrtrrNm.deleter
	def ChrtrrNm(self):
		del self._ChrtrrNm
		self._ChrtrrNm = base_types.UninitialisedField(self, 'ChrtrrNm', Max70Text, False)

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
	def IMONb(self):
		return self._IMONb

	@IMONb.setter
	def IMONb(self, value):
		self._IMONb = value if value is not None else base_types.UninitialisedField(self, 'IMONb', Exact7NumericText, False)

	@IMONb.deleter
	def IMONb(self):
		del self._IMONb
		self._IMONb = base_types.UninitialisedField(self, 'IMONb', Exact7NumericText, False)

	@property
	def MstrNm(self):
		return self._MstrNm

	@MstrNm.setter
	def MstrNm(self, value):
		self._MstrNm = value if value is not None else base_types.UninitialisedField(self, 'MstrNm', Max70Text, False)

	@MstrNm.deleter
	def MstrNm(self):
		del self._MstrNm
		self._MstrNm = base_types.UninitialisedField(self, 'MstrNm', Max70Text, False)

	@property
	def OwnrNm(self):
		return self._OwnrNm

	@OwnrNm.setter
	def OwnrNm(self, value):
		self._OwnrNm = value if value is not None else base_types.UninitialisedField(self, 'OwnrNm', Max70Text, False)

	@OwnrNm.deleter
	def OwnrNm(self):
		del self._OwnrNm
		self._OwnrNm = base_types.UninitialisedField(self, 'OwnrNm', Max70Text, False)

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

	@property
	def VygNb(self):
		return self._VygNb

	@VygNb.setter
	def VygNb(self, value):
		self._VygNb = value if value is not None else base_types.UninitialisedField(self, 'VygNb', Max35Text, False)

	@VygNb.deleter
	def VygNb(self):
		del self._VygNb
		self._VygNb = base_types.UninitialisedField(self, 'VygNb', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ChrtrrNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrrierAgtCtry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrrierAgtNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IMONb', type=Exact7NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MstrNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OwnrNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PortOfDschrge', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PortOfLoadng', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeaCrrierCtry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeaCrrierNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VsslNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VygNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))