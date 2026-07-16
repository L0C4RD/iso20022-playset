# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Address2
from . import ContactBusiness1
from . import ISODateTime
from . import JourneyType1Code
from . import Max35Text
from . import TimeSegment1Code

class ServiceStartEnd3(base_types._BaseFieldType):

	__slots__ = ["_Adr", "_Ctct", "_DtAndTm", "_JrnyData", "_JrnyDtAndTm", "_JrnyTp", "_Lctn", "_LctnCd", "_TmSgmt"]
	@property
	def Adr(self):
		return self._Adr

	@Adr.setter
	def Adr(self, value):
		self._Adr = value if value is not None else base_types.UninitialisedField(self, 'Adr', Address2, False)

	@Adr.deleter
	def Adr(self):
		del self._Adr
		self._Adr = base_types.UninitialisedField(self, 'Adr', Address2, False)

	@property
	def Ctct(self):
		return self._Ctct

	@Ctct.setter
	def Ctct(self, value):
		self._Ctct = value if value is not None else base_types.UninitialisedField(self, 'Ctct', ContactBusiness1, False)

	@Ctct.deleter
	def Ctct(self):
		del self._Ctct
		self._Ctct = base_types.UninitialisedField(self, 'Ctct', ContactBusiness1, False)

	@property
	def DtAndTm(self):
		return self._DtAndTm

	@DtAndTm.setter
	def DtAndTm(self, value):
		self._DtAndTm = value if value is not None else base_types.UninitialisedField(self, 'DtAndTm', ISODateTime, False)

	@DtAndTm.deleter
	def DtAndTm(self):
		del self._DtAndTm
		self._DtAndTm = base_types.UninitialisedField(self, 'DtAndTm', ISODateTime, False)

	@property
	def JrnyData(self):
		return self._JrnyData

	@JrnyData.setter
	def JrnyData(self, value):
		self._JrnyData = value if value is not None else base_types.UninitialisedField(self, 'JrnyData', Max35Text, False)

	@JrnyData.deleter
	def JrnyData(self):
		del self._JrnyData
		self._JrnyData = base_types.UninitialisedField(self, 'JrnyData', Max35Text, False)

	@property
	def JrnyDtAndTm(self):
		return self._JrnyDtAndTm

	@JrnyDtAndTm.setter
	def JrnyDtAndTm(self, value):
		self._JrnyDtAndTm = value if value is not None else base_types.UninitialisedField(self, 'JrnyDtAndTm', ISODateTime, False)

	@JrnyDtAndTm.deleter
	def JrnyDtAndTm(self):
		del self._JrnyDtAndTm
		self._JrnyDtAndTm = base_types.UninitialisedField(self, 'JrnyDtAndTm', ISODateTime, False)

	@property
	def JrnyTp(self):
		return self._JrnyTp

	@JrnyTp.setter
	def JrnyTp(self, value):
		self._JrnyTp = value if value is not None else base_types.UninitialisedField(self, 'JrnyTp', JourneyType1Code, False)

	@JrnyTp.deleter
	def JrnyTp(self):
		del self._JrnyTp
		self._JrnyTp = base_types.UninitialisedField(self, 'JrnyTp', JourneyType1Code, False)

	@property
	def Lctn(self):
		return self._Lctn

	@Lctn.setter
	def Lctn(self, value):
		self._Lctn = value if value is not None else base_types.UninitialisedField(self, 'Lctn', Max35Text, False)

	@Lctn.deleter
	def Lctn(self):
		del self._Lctn
		self._Lctn = base_types.UninitialisedField(self, 'Lctn', Max35Text, False)

	@property
	def LctnCd(self):
		return self._LctnCd

	@LctnCd.setter
	def LctnCd(self, value):
		self._LctnCd = value if value is not None else base_types.UninitialisedField(self, 'LctnCd', Max35Text, False)

	@LctnCd.deleter
	def LctnCd(self):
		del self._LctnCd
		self._LctnCd = base_types.UninitialisedField(self, 'LctnCd', Max35Text, False)

	@property
	def TmSgmt(self):
		return self._TmSgmt

	@TmSgmt.setter
	def TmSgmt(self, value):
		self._TmSgmt = value if value is not None else base_types.UninitialisedField(self, 'TmSgmt', TimeSegment1Code, False)

	@TmSgmt.deleter
	def TmSgmt(self):
		del self._TmSgmt
		self._TmSgmt = base_types.UninitialisedField(self, 'TmSgmt', TimeSegment1Code, False)

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