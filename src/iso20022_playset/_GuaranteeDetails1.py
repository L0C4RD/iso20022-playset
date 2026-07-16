# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndPeriod1
from . import Max2000Text
from . import PercentageAndPeriod1
from . import xs:IDREF
from . import xs:positiveInteger

class GuaranteeDetails1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_AssoctdDoc", "_CvrdPctg", "_Desc", "_GrntedAmt", "_Issr", "_Pos", "_Xcss"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max2000Text, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max2000Text, True)

	@property
	def AssoctdDoc(self):
		return self._AssoctdDoc

	@AssoctdDoc.setter
	def AssoctdDoc(self, value):
		self._AssoctdDoc = value if value is not None else base_types.UninitialisedField(self, 'AssoctdDoc', xs:IDREF, True)

	@AssoctdDoc.deleter
	def AssoctdDoc(self):
		del self._AssoctdDoc
		self._AssoctdDoc = base_types.UninitialisedField(self, 'AssoctdDoc', xs:IDREF, True)

	@property
	def CvrdPctg(self):
		return self._CvrdPctg

	@CvrdPctg.setter
	def CvrdPctg(self, value):
		self._CvrdPctg = value if value is not None else base_types.UninitialisedField(self, 'CvrdPctg', PercentageAndPeriod1, True)

	@CvrdPctg.deleter
	def CvrdPctg(self):
		del self._CvrdPctg
		self._CvrdPctg = base_types.UninitialisedField(self, 'CvrdPctg', PercentageAndPeriod1, True)

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if value is not None else base_types.UninitialisedField(self, 'Desc', Max2000Text, False)

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = base_types.UninitialisedField(self, 'Desc', Max2000Text, False)

	@property
	def GrntedAmt(self):
		return self._GrntedAmt

	@GrntedAmt.setter
	def GrntedAmt(self, value):
		self._GrntedAmt = value if value is not None else base_types.UninitialisedField(self, 'GrntedAmt', AmountAndPeriod1, True)

	@GrntedAmt.deleter
	def GrntedAmt(self):
		del self._GrntedAmt
		self._GrntedAmt = base_types.UninitialisedField(self, 'GrntedAmt', AmountAndPeriod1, True)

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if value is not None else base_types.UninitialisedField(self, 'Issr', xs:IDREF, False)

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = base_types.UninitialisedField(self, 'Issr', xs:IDREF, False)

	@property
	def Pos(self):
		return self._Pos

	@Pos.setter
	def Pos(self, value):
		self._Pos = value if value is not None else base_types.UninitialisedField(self, 'Pos', xs:positiveInteger, False)

	@Pos.deleter
	def Pos(self):
		del self._Pos
		self._Pos = base_types.UninitialisedField(self, 'Pos', xs:positiveInteger, False)

	@property
	def Xcss(self):
		return self._Xcss

	@Xcss.setter
	def Xcss(self, value):
		self._Xcss = value if value is not None else base_types.UninitialisedField(self, 'Xcss', AmountAndPeriod1, True)

	@Xcss.deleter
	def Xcss(self):
		del self._Xcss
		self._Xcss = base_types.UninitialisedField(self, 'Xcss', AmountAndPeriod1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='AssoctdDoc', type=XS_IDREF, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CvrdPctg', type=PercentageAndPeriod1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Desc', type=Max2000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrntedAmt', type=AmountAndPeriod1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Issr', type=XS_IDREF, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pos', type=XS_positiveInteger, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Xcss', type=AmountAndPeriod1, min=0, max=None, mutex_group=None, array=True),
	))