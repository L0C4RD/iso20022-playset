# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._GeographicPointInDecimalDegreesText import GeographicPointInDecimalDegreesText
from ._ISOCountrySubDivisionCode import ISOCountrySubDivisionCode
from ._ISOMax3ACountryCode import ISOMax3ACountryCode
from ._Max16Text import Max16Text
from ._Max50Text import Max50Text
from ._Max99Text import Max99Text

class Address4(base_types._BaseFieldType):

	__slots__ = ["_BldgNb", "_Ctry", "_CtrySubDvsnMjr", "_CtrySubDvsnMjrNm", "_CtrySubDvsnMnr", "_CtrySubDvsnMnrNm", "_GeogcLctn", "_Line1", "_Line2", "_PstlCd", "_StrtNm", "_TwnNm"]
	@property
	def BldgNb(self):
		return self._BldgNb

	@BldgNb.setter
	def BldgNb(self, value):
		self._BldgNb = value if type(value) != base_types.auto else self.make_default("BldgNb")

	@BldgNb.deleter
	def BldgNb(self):
		del self._BldgNb
		self._BldgNb = None

	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if type(value) != base_types.auto else self.make_default("Ctry")

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = None

	@property
	def CtrySubDvsnMjr(self):
		return self._CtrySubDvsnMjr

	@CtrySubDvsnMjr.setter
	def CtrySubDvsnMjr(self, value):
		self._CtrySubDvsnMjr = value if type(value) != base_types.auto else self.make_default("CtrySubDvsnMjr")

	@CtrySubDvsnMjr.deleter
	def CtrySubDvsnMjr(self):
		del self._CtrySubDvsnMjr
		self._CtrySubDvsnMjr = None

	@property
	def CtrySubDvsnMjrNm(self):
		return self._CtrySubDvsnMjrNm

	@CtrySubDvsnMjrNm.setter
	def CtrySubDvsnMjrNm(self, value):
		self._CtrySubDvsnMjrNm = value if type(value) != base_types.auto else self.make_default("CtrySubDvsnMjrNm")

	@CtrySubDvsnMjrNm.deleter
	def CtrySubDvsnMjrNm(self):
		del self._CtrySubDvsnMjrNm
		self._CtrySubDvsnMjrNm = None

	@property
	def CtrySubDvsnMnr(self):
		return self._CtrySubDvsnMnr

	@CtrySubDvsnMnr.setter
	def CtrySubDvsnMnr(self, value):
		self._CtrySubDvsnMnr = value if type(value) != base_types.auto else self.make_default("CtrySubDvsnMnr")

	@CtrySubDvsnMnr.deleter
	def CtrySubDvsnMnr(self):
		del self._CtrySubDvsnMnr
		self._CtrySubDvsnMnr = None

	@property
	def CtrySubDvsnMnrNm(self):
		return self._CtrySubDvsnMnrNm

	@CtrySubDvsnMnrNm.setter
	def CtrySubDvsnMnrNm(self, value):
		self._CtrySubDvsnMnrNm = value if type(value) != base_types.auto else self.make_default("CtrySubDvsnMnrNm")

	@CtrySubDvsnMnrNm.deleter
	def CtrySubDvsnMnrNm(self):
		del self._CtrySubDvsnMnrNm
		self._CtrySubDvsnMnrNm = None

	@property
	def GeogcLctn(self):
		return self._GeogcLctn

	@GeogcLctn.setter
	def GeogcLctn(self, value):
		self._GeogcLctn = value if type(value) != base_types.auto else self.make_default("GeogcLctn")

	@GeogcLctn.deleter
	def GeogcLctn(self):
		del self._GeogcLctn
		self._GeogcLctn = None

	@property
	def Line1(self):
		return self._Line1

	@Line1.setter
	def Line1(self, value):
		self._Line1 = value if type(value) != base_types.auto else self.make_default("Line1")

	@Line1.deleter
	def Line1(self):
		del self._Line1
		self._Line1 = None

	@property
	def Line2(self):
		return self._Line2

	@Line2.setter
	def Line2(self, value):
		self._Line2 = value if type(value) != base_types.auto else self.make_default("Line2")

	@Line2.deleter
	def Line2(self):
		del self._Line2
		self._Line2 = None

	@property
	def PstlCd(self):
		return self._PstlCd

	@PstlCd.setter
	def PstlCd(self, value):
		self._PstlCd = value if type(value) != base_types.auto else self.make_default("PstlCd")

	@PstlCd.deleter
	def PstlCd(self):
		del self._PstlCd
		self._PstlCd = None

	@property
	def StrtNm(self):
		return self._StrtNm

	@StrtNm.setter
	def StrtNm(self, value):
		self._StrtNm = value if type(value) != base_types.auto else self.make_default("StrtNm")

	@StrtNm.deleter
	def StrtNm(self):
		del self._StrtNm
		self._StrtNm = None

	@property
	def TwnNm(self):
		return self._TwnNm

	@TwnNm.setter
	def TwnNm(self, value):
		self._TwnNm = value if type(value) != base_types.auto else self.make_default("TwnNm")

	@TwnNm.deleter
	def TwnNm(self):
		del self._TwnNm
		self._TwnNm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BldgNb', type=Max16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctry', type=ISOMax3ACountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrySubDvsnMjr', type=ISOCountrySubDivisionCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrySubDvsnMjrNm', type=Max50Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrySubDvsnMnr', type=ISOCountrySubDivisionCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrySubDvsnMnrNm', type=Max50Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GeogcLctn', type=GeographicPointInDecimalDegreesText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Line1', type=Max99Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Line2', type=Max99Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstlCd', type=Max16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StrtNm', type=Max99Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TwnNm', type=Max50Text, min=0, max=1, mutex_group=None, array=False),
	))