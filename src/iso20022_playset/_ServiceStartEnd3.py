# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Address2 import Address2
from ._ContactBusiness1 import ContactBusiness1
from ._ISODateTime import ISODateTime
from ._JourneyType1Code import JourneyType1Code
from ._Max35Text import Max35Text
from ._TimeSegment1Code import TimeSegment1Code

class ServiceStartEnd3(base_types._BaseFieldType):

	__slots__ = ["_Adr", "_Ctct", "_DtAndTm", "_JrnyData", "_JrnyDtAndTm", "_JrnyTp", "_Lctn", "_LctnCd", "_TmSgmt"]
	@property
	def Adr(self):
		return self._Adr

	@Adr.setter
	def Adr(self, value):
		self._Adr = value if type(value) != base_types.auto else self.make_default("Adr")

	@Adr.deleter
	def Adr(self):
		del self._Adr
		self._Adr = None

	@property
	def Ctct(self):
		return self._Ctct

	@Ctct.setter
	def Ctct(self, value):
		self._Ctct = value if type(value) != base_types.auto else self.make_default("Ctct")

	@Ctct.deleter
	def Ctct(self):
		del self._Ctct
		self._Ctct = None

	@property
	def DtAndTm(self):
		return self._DtAndTm

	@DtAndTm.setter
	def DtAndTm(self, value):
		self._DtAndTm = value if type(value) != base_types.auto else self.make_default("DtAndTm")

	@DtAndTm.deleter
	def DtAndTm(self):
		del self._DtAndTm
		self._DtAndTm = None

	@property
	def JrnyData(self):
		return self._JrnyData

	@JrnyData.setter
	def JrnyData(self, value):
		self._JrnyData = value if type(value) != base_types.auto else self.make_default("JrnyData")

	@JrnyData.deleter
	def JrnyData(self):
		del self._JrnyData
		self._JrnyData = None

	@property
	def JrnyDtAndTm(self):
		return self._JrnyDtAndTm

	@JrnyDtAndTm.setter
	def JrnyDtAndTm(self, value):
		self._JrnyDtAndTm = value if type(value) != base_types.auto else self.make_default("JrnyDtAndTm")

	@JrnyDtAndTm.deleter
	def JrnyDtAndTm(self):
		del self._JrnyDtAndTm
		self._JrnyDtAndTm = None

	@property
	def JrnyTp(self):
		return self._JrnyTp

	@JrnyTp.setter
	def JrnyTp(self, value):
		self._JrnyTp = value if type(value) != base_types.auto else self.make_default("JrnyTp")

	@JrnyTp.deleter
	def JrnyTp(self):
		del self._JrnyTp
		self._JrnyTp = None

	@property
	def Lctn(self):
		return self._Lctn

	@Lctn.setter
	def Lctn(self, value):
		self._Lctn = value if type(value) != base_types.auto else self.make_default("Lctn")

	@Lctn.deleter
	def Lctn(self):
		del self._Lctn
		self._Lctn = None

	@property
	def LctnCd(self):
		return self._LctnCd

	@LctnCd.setter
	def LctnCd(self, value):
		self._LctnCd = value if type(value) != base_types.auto else self.make_default("LctnCd")

	@LctnCd.deleter
	def LctnCd(self):
		del self._LctnCd
		self._LctnCd = None

	@property
	def TmSgmt(self):
		return self._TmSgmt

	@TmSgmt.setter
	def TmSgmt(self, value):
		self._TmSgmt = value if type(value) != base_types.auto else self.make_default("TmSgmt")

	@TmSgmt.deleter
	def TmSgmt(self):
		del self._TmSgmt
		self._TmSgmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Adr', type=Address2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctct', type=ContactBusiness1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtAndTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='JrnyData', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='JrnyDtAndTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='JrnyTp', type=JourneyType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lctn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LctnCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TmSgmt', type=TimeSegment1Code, min=0, max=1, mutex_group=None, array=False),
	))