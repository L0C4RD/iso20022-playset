# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CustomBasket4
from . import GenericIdentification184
from . import ISINOct2015Identifier
from . import IndexIdentification1
from . import Max52Text
from . import UnderlyingIdentification1Code
from . import UniqueProductIdentifier2Choice

class SecurityIdentification41Choice(base_types._BaseFieldType):

	__slots__ = ["_AltrntvInstrmId", "_Bskt", "_ISIN", "_IdNotAvlbl", "_Indx", "_Othr", "_UnqPdctIdr"]
	@property
	def AltrntvInstrmId(self):
		return self._AltrntvInstrmId

	@AltrntvInstrmId.setter
	def AltrntvInstrmId(self, value):
		self._AltrntvInstrmId = value if value is not None else base_types.UninitialisedField(self, 'AltrntvInstrmId', Max52Text, False)

	@AltrntvInstrmId.deleter
	def AltrntvInstrmId(self):
		del self._AltrntvInstrmId
		self._AltrntvInstrmId = base_types.UninitialisedField(self, 'AltrntvInstrmId', Max52Text, False)

	@property
	def Bskt(self):
		return self._Bskt

	@Bskt.setter
	def Bskt(self, value):
		self._Bskt = value if value is not None else base_types.UninitialisedField(self, 'Bskt', CustomBasket4, False)

	@Bskt.deleter
	def Bskt(self):
		del self._Bskt
		self._Bskt = base_types.UninitialisedField(self, 'Bskt', CustomBasket4, False)

	@property
	def ISIN(self):
		return self._ISIN

	@ISIN.setter
	def ISIN(self, value):
		self._ISIN = value if value is not None else base_types.UninitialisedField(self, 'ISIN', ISINOct2015Identifier, False)

	@ISIN.deleter
	def ISIN(self):
		del self._ISIN
		self._ISIN = base_types.UninitialisedField(self, 'ISIN', ISINOct2015Identifier, False)

	@property
	def IdNotAvlbl(self):
		return self._IdNotAvlbl

	@IdNotAvlbl.setter
	def IdNotAvlbl(self, value):
		self._IdNotAvlbl = value if value is not None else base_types.UninitialisedField(self, 'IdNotAvlbl', UnderlyingIdentification1Code, False)

	@IdNotAvlbl.deleter
	def IdNotAvlbl(self):
		del self._IdNotAvlbl
		self._IdNotAvlbl = base_types.UninitialisedField(self, 'IdNotAvlbl', UnderlyingIdentification1Code, False)

	@property
	def Indx(self):
		return self._Indx

	@Indx.setter
	def Indx(self, value):
		self._Indx = value if value is not None else base_types.UninitialisedField(self, 'Indx', IndexIdentification1, False)

	@Indx.deleter
	def Indx(self):
		del self._Indx
		self._Indx = base_types.UninitialisedField(self, 'Indx', IndexIdentification1, False)

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if value is not None else base_types.UninitialisedField(self, 'Othr', GenericIdentification184, False)

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = base_types.UninitialisedField(self, 'Othr', GenericIdentification184, False)

	@property
	def UnqPdctIdr(self):
		return self._UnqPdctIdr

	@UnqPdctIdr.setter
	def UnqPdctIdr(self, value):
		self._UnqPdctIdr = value if value is not None else base_types.UninitialisedField(self, 'UnqPdctIdr', UniqueProductIdentifier2Choice, False)

	@UnqPdctIdr.deleter
	def UnqPdctIdr(self):
		del self._UnqPdctIdr
		self._UnqPdctIdr = base_types.UninitialisedField(self, 'UnqPdctIdr', UniqueProductIdentifier2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AltrntvInstrmId', type=Max52Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Bskt', type=CustomBasket4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ISIN', type=ISINOct2015Identifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IdNotAvlbl', type=UnderlyingIdentification1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Indx', type=IndexIdentification1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Othr', type=GenericIdentification184, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='UnqPdctIdr', type=UniqueProductIdentifier2Choice, min=0, max=1, mutex_group=1, array=False),
	))