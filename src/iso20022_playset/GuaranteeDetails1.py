import base_types
import Max2000Text
import xs:IDREF
import xs:positiveInteger
import AmountAndPeriod1
import PercentageAndPeriod1

class GuaranteeDetails1(base_types._BaseFieldType):

	__slots__ = ["_Xcss", "_Issr", "_AddtlInf", "_Pos", "_GrntedAmt", "_CvrdPctg", "_AssoctdDoc", "_Desc"]
	@property
	def Xcss(self):
		return self._Xcss

	@Xcss.setter
	def Xcss(self, value):
		self._Xcss = value if type(value) != auto else self.make_default("Xcss")

	@Xcss.deleter
	def Xcss(self):
		del self._Xcss
		self._Xcss = None

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if type(value) != auto else self.make_default("Issr")

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def Pos(self):
		return self._Pos

	@Pos.setter
	def Pos(self, value):
		self._Pos = value if type(value) != auto else self.make_default("Pos")

	@Pos.deleter
	def Pos(self):
		del self._Pos
		self._Pos = None

	@property
	def GrntedAmt(self):
		return self._GrntedAmt

	@GrntedAmt.setter
	def GrntedAmt(self, value):
		self._GrntedAmt = value if type(value) != auto else self.make_default("GrntedAmt")

	@GrntedAmt.deleter
	def GrntedAmt(self):
		del self._GrntedAmt
		self._GrntedAmt = None

	@property
	def CvrdPctg(self):
		return self._CvrdPctg

	@CvrdPctg.setter
	def CvrdPctg(self, value):
		self._CvrdPctg = value if type(value) != auto else self.make_default("CvrdPctg")

	@CvrdPctg.deleter
	def CvrdPctg(self):
		del self._CvrdPctg
		self._CvrdPctg = None

	@property
	def AssoctdDoc(self):
		return self._AssoctdDoc

	@AssoctdDoc.setter
	def AssoctdDoc(self, value):
		self._AssoctdDoc = value if type(value) != auto else self.make_default("AssoctdDoc")

	@AssoctdDoc.deleter
	def AssoctdDoc(self):
		del self._AssoctdDoc
		self._AssoctdDoc = None

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if type(value) != auto else self.make_default("Desc")

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Xcss', type=AmountAndPeriod1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Issr', type=XS_IDREF, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='Pos', type=XS_positiveInteger, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrntedAmt', type=AmountAndPeriod1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CvrdPctg', type=PercentageAndPeriod1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AssoctdDoc', type=XS_IDREF, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Desc', type=Max2000Text, min=0, max=1, mutex_group=None, array=False),
	))

