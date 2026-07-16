# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ExternalChannel1Code
from . import Max140Text
from . import PartyType1Choice
from . import PostalAddress6

class CommunicationChannel1(base_types._BaseFieldType):

	__slots__ = ["_DlvrToAdr", "_DlvrToNm", "_DlvrToPtyTp", "_Mtd"]
	@property
	def DlvrToAdr(self):
		return self._DlvrToAdr

	@DlvrToAdr.setter
	def DlvrToAdr(self, value):
		self._DlvrToAdr = value if value is not None else base_types.UninitialisedField(self, 'DlvrToAdr', PostalAddress6, False)

	@DlvrToAdr.deleter
	def DlvrToAdr(self):
		del self._DlvrToAdr
		self._DlvrToAdr = base_types.UninitialisedField(self, 'DlvrToAdr', PostalAddress6, False)

	@property
	def DlvrToNm(self):
		return self._DlvrToNm

	@DlvrToNm.setter
	def DlvrToNm(self, value):
		self._DlvrToNm = value if value is not None else base_types.UninitialisedField(self, 'DlvrToNm', Max140Text, False)

	@DlvrToNm.deleter
	def DlvrToNm(self):
		del self._DlvrToNm
		self._DlvrToNm = base_types.UninitialisedField(self, 'DlvrToNm', Max140Text, False)

	@property
	def DlvrToPtyTp(self):
		return self._DlvrToPtyTp

	@DlvrToPtyTp.setter
	def DlvrToPtyTp(self, value):
		self._DlvrToPtyTp = value if value is not None else base_types.UninitialisedField(self, 'DlvrToPtyTp', PartyType1Choice, False)

	@DlvrToPtyTp.deleter
	def DlvrToPtyTp(self):
		del self._DlvrToPtyTp
		self._DlvrToPtyTp = base_types.UninitialisedField(self, 'DlvrToPtyTp', PartyType1Choice, False)

	@property
	def Mtd(self):
		return self._Mtd

	@Mtd.setter
	def Mtd(self, value):
		self._Mtd = value if value is not None else base_types.UninitialisedField(self, 'Mtd', ExternalChannel1Code, False)

	@Mtd.deleter
	def Mtd(self):
		del self._Mtd
		self._Mtd = base_types.UninitialisedField(self, 'Mtd', ExternalChannel1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DlvrToAdr', type=PostalAddress6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvrToNm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvrToPtyTp', type=PartyType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mtd', type=ExternalChannel1Code, min=1, max=1, mutex_group=None, array=False),
	))